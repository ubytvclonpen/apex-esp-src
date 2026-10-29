"""Ties together the ESP renderer, aimbot controller and process bridge."""
from __future__ import annotations

import threading
import time

from apex_esp.core.config.schema import EspConfig
from apex_esp.core.models.player import PlayerSnapshot
from apex_esp.features.aimbot.controller import AimbotController
from apex_esp.features.esp.renderer import EspRenderer
from apex_esp.infra.driver_bridge import DriverBridge


class OverlayOrchestrator:
    def __init__(self, cfg: EspConfig) -> None:
        self.cfg = cfg
        self.bridge = DriverBridge(cfg.bridge)
        self.renderer = EspRenderer(cfg.renderer)
        self.aimbot = AimbotController(cfg.aimbot)
        self._stop = threading.Event()
        self._worker: threading.Thread | None = None

    def _tick(self) -> None:
        while not self._stop.is_set():
            snap = self.bridge.read_entities()
            players: list[PlayerSnapshot] = snap.players
            self.renderer.draw(players, snap.local_view)
            self.aimbot.step(players, snap.local_view)
            time.sleep(self.cfg.tick_interval_ms / 1000.0)

    def run(self) -> None:
        self.bridge.attach()
        self.renderer.init()
        self._worker = threading.Thread(target=self._tick, name="esp-tick", daemon=True)
        self._worker.start()
        self._worker.join()

    def teardown(self) -> None:
        self._stop.set()
        if self._worker:
            self._worker.join(timeout=2.0)
        self.renderer.shutdown()
        self.bridge.detach()