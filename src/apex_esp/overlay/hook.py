"""d3d11 Present hook used by the ESP renderer."""
from __future__ import annotations

from typing import Callable

PresentCallback = Callable[[object], None]


class PresentHook:
    def __init__(self) -> None:
        self._callbacks: list[PresentCallback] = []
        self._installed = False

    def add(self, cb: PresentCallback) -> None:
        self._callbacks.append(cb)

    def install(self) -> None:
        # vtable patch on IDXGISwapChain::Present
        self._installed = True

    def uninstall(self) -> None:
        self._installed = False

    def _dispatch(self, swapchain: object) -> None:
        for cb in self._callbacks:
            cb(swapchain)