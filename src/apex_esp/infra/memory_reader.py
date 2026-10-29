"""Thin wrapper around ReadProcessMemory for the entity loop."""
from __future__ import annotations

import ctypes
from ctypes import wintypes

PROCESS_VM_READ = 0x0010
PROCESS_QUERY_INFORMATION = 0x0400


class MemoryReader:
    def __init__(self, pid: int) -> None:
        self.pid = pid
        self._handle: int | None = None

    def open(self) -> None:
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        self._handle = k32.OpenProcess(
            PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, False, self.pid
        )
        if not self._handle:
            raise OSError(ctypes.get_last_error(), "OpenProcess failed")

    def read(self, addr: int, size: int) -> bytes:
        buf = (ctypes.c_char * size)()
        read = wintypes.SIZE_T(0)
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        ok = k32.ReadProcessMemory(
            self._handle, ctypes.c_void_p(addr), buf, size, ctypes.byref(read)
        )
        if not ok:
            raise OSError(ctypes.get_last_error(), "ReadProcessMemory failed")
        return bytes(buf)

    def close(self) -> None:
        if self._handle:
            ctypes.WinDLL("kernel32").CloseHandle(self._handle)
            self._handle = None