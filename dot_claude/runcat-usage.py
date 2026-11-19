#!/usr/bin/python3
"""Claude のプラン利用率を Anthropic の usage API から取得し、RunCat Neo の Custom Metrics に書き出す。"""

import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path


OUT = Path(os.environ.get("RUNCAT_OUT_FILE", str(Path.home() / ".claude" / "runcat-usage.json")))
USAGE_URL = "https://api.anthropic.com/api/oauth/usage"
KEYCHAIN_SERVICE = "Claude Code-credentials"
JST = timezone(timedelta(hours=9), name="JST")
JAPANESE_WEEKDAYS = "月火水木金土日"
WINDOWS = (("5h", "five_hour"), ("7d", "seven_day"))


def percentage_metric(title, used_percentage):
    if not isinstance(used_percentage, (int, float)) or isinstance(used_percentage, bool):
        return None
    clamped_percentage = max(0.0, min(float(used_percentage), 100.0))
    normalized_value = clamped_percentage / 100
    formatted_percentage = f"{clamped_percentage:.1f}".rstrip("0").rstrip(".")
    return {
        "title": title,
        "formattedValue": f"{formatted_percentage}%",
        "normalizedValue": round(normalized_value, 4),
    }


def reset_metric(title, resets_at):
    if not isinstance(resets_at, str):
        return None
    try:
        reset_at = datetime.fromisoformat(resets_at).astimezone(JST)
    except ValueError:
        return None
    return {
        "title": f"{title} リセット",
        "formattedValue": (
            f"{reset_at.month}/{reset_at.day}"
            f"({JAPANESE_WEEKDAYS[reset_at.weekday()]}) {reset_at:%H:%M}"
        ),
    }


def access_token():
    credentials = subprocess.run(
        ["/usr/bin/security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
        capture_output=True,
        text=True,
        timeout=10,
        check=True,
    ).stdout
    oauth = json.loads(credentials).get("claudeAiOauth") or {}
    token = oauth.get("accessToken")
    expires_at = oauth.get("expiresAt")
    # トークンの更新は Claude Code 本体に任せ、期限切れの間は取得を見送る。
    if not token or (isinstance(expires_at, (int, float)) and expires_at / 1000 <= time.time()):
        return None
    return token


def fetch_usage(token):
    # トークンをプロセス一覧に出さないよう、ヘッダーは stdin から curl に渡す。
    response = subprocess.run(
        [
            "/usr/bin/curl", "-sS", "--fail", "--max-time", "15",
            "-H", "@-",
            "-H", "anthropic-beta: oauth-2025-04-20",
            USAGE_URL,
        ],
        input=f"Authorization: Bearer {token}\n",
        capture_output=True,
        text=True,
        timeout=20,
        check=True,
    ).stdout
    return json.loads(response)


def rate_limit_metrics(usage):
    metrics = []
    for title, key in WINDOWS:
        limit = usage.get(key) or {}
        metric = percentage_metric(title, limit.get("utilization"))
        if metric is None:
            continue
        metrics.append(metric)
        reset = reset_metric(title, limit.get("resets_at"))
        if reset is not None:
            metrics.append(reset)
    return metrics


def write_snapshot(usage):
    rate_metrics = rate_limit_metrics(usage)
    if not rate_metrics:
        return
    snapshot = {
        "title": "Claude",
        "symbol": "sparkle",
        "metrics": rate_metrics,
        "lastUpdatedDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    snapshot["metricsBarValue"] = rate_metrics[0]["formattedValue"]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, temporary_path = tempfile.mkstemp(prefix=".runcat-", dir=str(OUT.parent))
    try:
        with os.fdopen(file_descriptor, "w", encoding="utf-8") as output:
            json.dump(snapshot, output, ensure_ascii=False)
        os.replace(temporary_path, OUT)
    except Exception:
        try:
            os.unlink(temporary_path)
        except OSError:
            pass
        raise


def main():
    try:
        token = access_token()
        if token is not None:
            write_snapshot(fetch_usage(token))
    except subprocess.CalledProcessError as error:
        # コマンドラインや認証情報をログに残さない。
        print(f"RunCat Claude usage: {error.cmd[0]} exited with {error.returncode}", file=sys.stderr)
    except Exception as error:
        print(f"RunCat Claude usage: {type(error).__name__}: {error}", file=sys.stderr)


if __name__ == "__main__":
    main()
