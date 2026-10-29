"""Runtime checks for the Windows overlay dependencies."""
from __future__ import annotations

import ctypes
import platform


def ensure_directx_runtime() -> bool:
    if platform.system() != "Windows":
        return False
    try:
        ctypes.WinDLL("d3d11.dll")
        return True
    except OSError:
        return False