#!/usr/bin/env python3
"""Claude Code利用率のRunCat連携を現在のMacへ導入する。"""

import os
import plistlib
import subprocess
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent.parent / "dot_claude/runcat-t3-usage.py"
    label = "local.runcat.claude-usage"
    agents = Path.home() / "Library/LaunchAgents"
    agents.mkdir(parents=True, exist_ok=True)
    agent = agents / f"{label}.plist"
    # Homebrewのバージョン付きパスはPython更新で消えるため、macOS標準を優先する。
    python = "/usr/bin/python3" if Path("/usr/bin/python3").exists() else sys.executable
    job = {
        "Label": label,
        "ProgramArguments": [python, str(source)],
        "RunAtLoad": True,
        "StartInterval": 30,
        "StandardErrorPath": str(Path.home() / ".claude/runcat-t3-error.log"),
    }
    (Path.home() / ".claude").mkdir(parents=True, exist_ok=True)
    with agent.open("wb") as output:
        plistlib.dump(job, output)
    domain = f"gui/{os.getuid()}"
    subprocess.run(["launchctl", "bootout", f"{domain}/{label}"], capture_output=True)
    subprocess.run(["launchctl", "bootstrap", domain, str(agent)], check=True)
    subprocess.run([python, str(source)], check=True)
    print("Claude Code利用率を30秒ごとにRunCatへ反映する設定を導入しました。")


if __name__ == "__main__":
    main()
