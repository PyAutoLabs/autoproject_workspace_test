#!/usr/bin/env python3
"""Minimal smoke runner: execute every script listed in smoke_tests.txt
(repo-root-relative, one per line, # comments allowed); fail on the first
nonzero exit. The reusable Smoke Tests workflow invokes this."""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TIMEOUT = int(os.environ.get("SMOKE_TIMEOUT_SECS", "600"))

env = dict(os.environ, MPLBACKEND="Agg")
scripts = [
    line.strip()
    for line in (ROOT / "smoke_tests.txt").read_text().splitlines()
    if line.strip() and not line.strip().startswith("#")
]
for script in scripts:
    print(f"== smoke: {script}", flush=True)
    result = subprocess.run(
        [sys.executable, script], cwd=ROOT, env=env, timeout=TIMEOUT
    )
    if result.returncode != 0:
        sys.exit(f"smoke FAILED: {script} (exit {result.returncode})")
print(f"smoke OK: {len(scripts)} script(s)")
