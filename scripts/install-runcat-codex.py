#!/usr/bin/env python3
"""Codex利用率のRunCat連携を現在のMacへ導入する。"""

import os
import plistlib
import subprocess
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent.parent / "dot_codex/runcat-usage.py"
    label = "local.runcat.codex-usage"
    agents = Path.home() / "Library/LaunchAgents"
    agents.mkdir(parents=True, exist_ok=True)
    agent = agents / f"{label}.plist"
    # Homebrewのバージョン付きパスはPython更新で消えるため、macOS標準を優先する。
    python = "/usr/bin/python3" if Path("/usr/bin/python3").exists() else sys.executable
    job = {
        "Label": label,
        "ProgramArguments": [python, "-I", str(source)],
        "RunAtLoad": True,
        # 非公開APIへの問い合わせなので、Codex本体の更新頻度に近い5分間隔に抑える。
        "StartInterval": 300,
        "StandardErrorPath": str(Path.home() / ".codex/runcat-usage-error.log"),
    }
    (Path.home() / ".codex").mkdir(parents=True, exist_ok=True)
    with agent.open("wb") as output:
        plistlib.dump(job, output)
    domain = f"gui/{os.getuid()}"
    subprocess.run(["launchctl", "bootout", f"{domain}/{label}"], capture_output=True)
    subprocess.run(["launchctl", "bootstrap", domain, str(agent)], check=True)
    subprocess.run([python, "-I", str(source)], check=True)
    print("Codex利用率を5分ごとにRunCatへ反映する設定を導入しました。")


if __name__ == "__main__":
    main()
