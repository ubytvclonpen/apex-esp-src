"""Bridge between the overlay process and the game memory reader."""
from __future__ import annotations

import logging

from apex_esp.core.config.schema import BridgeConfig
from apex_esp.core.models.player import PlayerSnapshot, Vec3
from apex_esp.core.models.world import LocalView, WorldSnapshot

log = logging.getLogger(__name__)


class DriverBridge:
    def __init__(self, cfg: BridgeConfig) -> None:
        self.cfg = cfg
        self._attached = False

    def attach(self) -> None:
        log.info("attaching to %s via %s backend", self.cfg.process, self.cfg.backend)
        self._attached = True

    def read_entities(self) -> WorldSnapshot:
        if not self._attached:
            return WorldSnapshot(local_view=LocalView(Vec3(0, 0, 0), 0, 0, 90), players=[])
        # real implementation reads via the km/usermode reader
        return WorldSnapshot(local_view=LocalView(Vec3(0, 0, 0), 0, 0, 90), players=[])

    def detach(self) -> None:
        self._attached = False