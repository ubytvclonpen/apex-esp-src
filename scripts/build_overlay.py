"""Build script that bundles the Python overlay with a d3d11 shim."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
BUILD = ROOT / "build"


def clean() -> None:
    for p in (DIST, BUILD):
        if p.exists():
            shutil.rmtree(p)


def freeze() -> None:
    subprocess.run(
        [sys.executable, "-m", "PyInstaller", "--noconfirm",
         "--name", "apex-esp", "src/apex_esp/app/bootstrap.py"],
        cwd=ROOT, check=True,
    )


if __name__ == "__main__":
    clean()
    freeze()
    print("build finished ->", DIST)