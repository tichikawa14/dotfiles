#!/usr/bin/python3
"""Codex の利用率を ChatGPT の usage API から取得し、RunCat Neo の Custom Metrics に書き出す。"""

import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path


CODEX_HOME = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
OUT = Path(os.environ.get("RUNCAT_OUT_FILE", str(CODEX_HOME / "runcat-usage.json")))
USAGE_URL = "https://chatgpt.com/backend-api/wham/usage"
JST = timezone(timedelta(hours=9), name="JST")
JAPANESE_WEEKDAYS = "月火水木金土日"
WINDOWS = ("primary_window", "secondary_window")


def percentage_metric(title, used_percentage):
    if not isinstance(used_percentage, (int, float)) or isinstance(used_percentage, bool):
        return None
    clamped_percentage = max(0.0, min(float(used_percentage), 100.0))
    formatted_percentage = f"{clamped_percentage:.1f}".rstrip("0").rstrip(".")
    return {
        "title": title,
        "formattedValue": f"{formatted_percentage}%",
        "normalizedValue": round(clamped_percentage / 100, 4),
    }


def window_title(window_seconds):
    if not isinstance(window_seconds, (int, float)) or isinstance(window_seconds, bool):
        return None
    minutes = window_seconds / 60
    if minutes % 1440 == 0:
        return f"{minutes / 1440:g}d"
    if minutes % 60 == 0:
        return f"{minutes / 60:g}h"
    return f"{minutes:g}m"


def reset_metric(title, resets_at):
    if not isinstance(resets_at, (int, float)) or isinstance(resets_at, bool):
        return None
    try:
        reset_at = datetime.fromtimestamp(resets_at, timezone.utc).astimezone(JST)
    except (OSError, OverflowError, ValueError):
        return None
    return {
        "title": f"{title} リセット",
        "formattedValue": (
            f"{reset_at.month}/{reset_at.day}"
            f"({JAPANESE_WEEKDAYS[reset_at.weekday()]}) {reset_at:%H:%M}"
        ),
    }


def jwt_expiry(token):
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload)).get("exp")
    except (IndexError, ValueError, AttributeError):
        return None


def credentials():
    tokens = json.loads((CODEX_HOME / "auth.json").read_text(encoding="utf-8")).get("tokens") or {}
    token = tokens.get("access_token")
    account_id = tokens.get("account_id")
    if not token or not account_id:
        return None
    # トークンの更新は Codex 本体に任せ、期限切れの間は取得を見送る。
    expires_at = jwt_expiry(token)
    if isinstance(expires_at, (int, float)) and expires_at <= time.time():
        return None
    return token, account_id


def fetch_usage(token, account_id):
    # トークンをプロセス一覧に出さないよう、ヘッダーは stdin から curl に渡す。
    response = subprocess.run(
        [
            "/usr/bin/curl", "-sS", "--fail", "--max-time", "15",
            "-H", "@-",
            "-H", "User-Agent: codex_cli_rs",
            USAGE_URL,
        ],
        input=f"Authorization: Bearer {token}\nChatGPT-Account-Id: {account_id}\n",
        capture_output=True,
        text=True,
        timeout=20,
        check=True,
    ).stdout
    return json.loads(response)


def configured_model():
    # /usr/bin/python3 は 3.9 で tomllib が無いため、先頭テーブルより前の model 行だけを読む。
    try:
        config = (CODEX_HOME / "config.toml").read_text(encoding="utf-8")
    except OSError:
        return None
    for line in config.splitlines():
        if line.lstrip().startswith("["):
            return None
        match = re.match(r'\s*model\s*=\s*"([^"]+)"', line)
        if match:
            return match.group(1)
    return None


def rate_limit_metrics(usage):
    rate_limit = usage.get("rate_limit") or {}
    metrics = []
    for key in WINDOWS:
        window = rate_limit.get(key) or {}
        title = window_title(window.get("limit_window_seconds"))
        metric = percentage_metric(title, window.get("used_percent")) if title else None
        if metric is None:
            continue
        metrics.append(metric)
        reset = reset_metric(title, window.get("reset_at"))
        if reset is not None:
            metrics.append(reset)
    return metrics


def write_snapshot(usage):
    rate_metrics = rate_limit_metrics(usage)
    if not rate_metrics:
        # 形式が変わって黙って止まると気付けないため、ログに残す。
        print("RunCat Codex usage: rate_limit が見つかりません", file=sys.stderr)
        return
    metrics = [{"title": "Model", "formattedValue": configured_model() or "Codex"}]
    metrics.extend(rate_metrics)
    snapshot = {
        "title": "Codex",
        "symbol": "camera.aperture",
        "metrics": metrics,
        "lastUpdatedDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "metricsBarValue": rate_metrics[0]["formattedValue"],
    }
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
        auth = credentials()
        if auth is not None:
            write_snapshot(fetch_usage(*auth))
    except subprocess.CalledProcessError as error:
        # コマンドラインや認証情報をログに残さない。
        print(f"RunCat Codex usage: {error.cmd[0]} exited with {error.returncode}", file=sys.stderr)
    except Exception as error:
        print(f"RunCat Codex usage: {type(error).__name__}: {error}", file=sys.stderr)


if __name__ == "__main__":
    main()
