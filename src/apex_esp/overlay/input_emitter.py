"""Synthetic mouse input used by the aimbot controller."""
from __future__ import annotations

import ctypes


class InputEmitter:
    def __init__(self) -> None:
        self._user32 = ctypes.WinDLL("user32", use_last_error=True)

    def move_relative(self, dx: int, dy: int) -> None:
        self._user32.mouse_event(0x0001, int(dx), int(dy), 0, 0)

    def left_click(self) -> None:
        self._user32.mouse_event(0x0002, 0, 0, 0, 0)
        self._user32.mouse_event(0x0004, 0, 0, 0, 0)