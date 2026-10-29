"""Overlay draw layer — boxes, skeletons, health bars."""
from __future__ import annotations

import logging

from apex_esp.core.config.schema import RendererConfig
from apex_esp.core.models.player import PlayerSnapshot
from apex_esp.core.models.world import LocalView

log = logging.getLogger(__name__)


class EspRenderer:
    def __init__(self, cfg: RendererConfig) -> None:
        self.cfg = cfg
        self._ready = False

    def init(self) -> None:
        log.info("renderer backend=%s initialising", self.cfg.backend)
        self._ready = True

    def draw(self, players: list[PlayerSnapshot], view: LocalView) -> None:
        if not self._ready:
            return
        for p in players:
            if not p.is_alive:
                continue
            self._draw_box(p)
            if self.cfg.skeleton:
                self._draw_skeleton(p)
            if self.cfg.health_bar:
                self._draw_health(p)

    def _draw_box(self, p: PlayerSnapshot) -> None:
        # screen projection happens inside the d3d11 hook; placeholder
        _ = (p.origin, self.cfg.box_color)

    def _draw_skeleton(self, p: PlayerSnapshot) -> None:
        for bone in p.bones:
            _ = bone.pos

    def _draw_health(self, p: PlayerSnapshot) -> None:
        _ = (p.health, p.shield)

    def shutdown(self) -> None:
        self._ready = False