#!/usr/bin/env python3
"""T3 Codeが取得したClaude Code利用率をRunCat Neoへ反映する。"""

import json
import math
import os
import re
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path


JST = timezone(timedelta(hours=9), name="JST")
WEEKDAYS = "月火水木金土日"
CACHE = Path(os.environ.get("RUNCAT_T3_CACHE", str(Path.home() / ".t3/caches/claudeAgent.json")))
OUT = Path(os.environ.get("RUNCAT_OUT_FILE", str(Path.home() / ".claude/runcat-usage.json")))


def parse_date(value):
    if not isinstance(value, str):
        raise ValueError("取得日時がありません")
    # Python 3.10以前のfromisoformatは小数秒の桁数に厳しいため、秒未満を落とす。
    result = datetime.fromisoformat(re.sub(r"\.\d+", "", value).replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("取得日時にタイムゾーンがありません")
    return result


def build_snapshot(cache):
    limits = cache.get("usageLimits") or {}
    checked_at = parse_date(limits.get("checkedAt"))
    metrics = []
    for window in limits.get("windows") or []:
        title = {"five_hour": "5h", "seven_day": "7d"}.get(window.get("id"))
        used = window.get("usedPercent")
        if not title or isinstance(used, bool) or not isinstance(used, (int, float)) or not math.isfinite(used):
            continue
        used = max(0.0, min(float(used), 100.0))
        percent = f"{used:.1f}".rstrip("0").rstrip(".")
        reset = None
        try:
            reset = parse_date(window.get("resetsAt")).astimezone(JST)
        except (ValueError, OverflowError):
            pass
        # キャッシュの値はリセット後の利用率を表さないため、期限切れを明示する。
        expired = reset is not None and reset <= datetime.now(timezone.utc)
        metric = {"title": title, "formattedValue": "更新待ち" if expired else f"{percent}%"}
        if not expired:
            metric["normalizedValue"] = round(used / 100, 4)
        metrics.append(metric)
        if reset is not None:
            metrics.append({
                "title": f"{title} リセット",
                "formattedValue": f"{reset.month}/{reset.day}({WEEKDAYS[reset.weekday()]}) {reset:%H:%M}",
            })
    if not metrics:
        return None
    return {
        "title": "Claude Code",
        "symbol": "staroflife",
        "metrics": metrics,
        "metricsBarValue": metrics[0]["formattedValue"],
        "lastUpdatedDate": checked_at.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def unavailable_snapshot():
    return {
        "title": "Claude Code",
        "symbol": "staroflife",
        "metrics": [{"title": "状態", "formattedValue": "未取得"}],
        "metricsBarValue": "未取得",
        "lastUpdatedDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def write_unavailable():
    # 古い利用率を残さないよう未取得に置き換える。既に未取得なら書き換えない。
    try:
        if json.loads(OUT.read_text(encoding="utf-8")).get("metricsBarValue") == "未取得":
            return
    except (OSError, ValueError, AttributeError):
        pass
    write(unavailable_snapshot())


def write(snapshot):
    serialized = json.dumps(snapshot, ensure_ascii=False, allow_nan=False)
    if OUT.exists() and OUT.read_text(encoding="utf-8") == serialized:
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_path = tempfile.mkstemp(prefix=".runcat-", dir=str(OUT.parent))
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as output:
            output.write(serialized)
        os.replace(temporary_path, OUT)
    finally:
        if os.path.exists(temporary_path):
            os.unlink(temporary_path)


def main():
    try:
        snapshot = build_snapshot(json.loads(CACHE.read_text(encoding="utf-8")))
    except FileNotFoundError:
        # T3 Codeを初めて使うまではキャッシュが存在しない。
        snapshot = None
    except (OSError, ValueError, TypeError, AttributeError) as error:
        print(f"RunCat T3 Code: {error}", file=sys.stderr)
        write_unavailable()
        sys.exit(1)
    if snapshot is None:
        write_unavailable()
    else:
        write(snapshot)


if __name__ == "__main__":
    main()
