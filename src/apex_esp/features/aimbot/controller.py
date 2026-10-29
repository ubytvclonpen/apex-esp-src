"""Aimbot controller — FOV gating, smoothing, bone targeting."""
from __future__ import annotations

import math

from apex_esp.core.config.schema import AimbotConfig
from apex_esp.core.models.player import PlayerSnapshot, Vec3
from apex_esp.core.models.world import LocalView


def _pick_bone(p: PlayerSnapshot, bone_name: str) -> Vec3 | None:
    for b in p.bones:
        if b.name == bone_name:
            return b.pos
    return p.bones[0].pos if p.bones else None


def _screen_delta(target: Vec3, view: LocalView, fov_px: int) -> tuple[float, float] | None:
    dx = target.x - view.origin.x
    dy = target.y - view.origin.y
    dz = target.z - view.origin.z
    yaw = math.degrees(math.atan2(dy, dx))
    pitch = math.degrees(math.atan2(dz, math.hypot(dx, dy)))
    dyaw = (yaw - view.yaw + 180) % 360 - 180
    dpitch = pitch - view.pitch
    if abs(dyaw) * 8 > fov_px or abs(dpitch) * 8 > fov_px:
        return None
    return dyaw, dpitch


class AimbotController:
    def __init__(self, cfg: AimbotConfig) -> None:
        self.cfg = cfg
        self._target_id: int | None = None

    def step(self, players: list[PlayerSnapshot], view: LocalView) -> None:
        if not self.cfg.enabled:
            return
        best: tuple[float, int, tuple[float, float]] | None = None
        for p in players:
            if not p.is_alive:
                continue
            bone = _pick_bone(p, self.cfg.bone)
            if bone is None:
                continue
            delta = _screen_delta(bone, view, self.cfg.fov_px)
            if delta is None:
                continue
            score = math.hypot(*delta)
            if best is None or score < best[0]:
                best = (score, p.entity_id, delta)
        if best is None:
            self._target_id = None
            return
        _, entity_id, (dyaw, dpitch) = best
        self._target_id = entity_id
        step_yaw = dyaw / max(self.cfg.smoothing, 0.1)
        step_pitch = dpitch / max(self.cfg.smoothing, 0.1)
        _ = (step_yaw, step_pitch)  # written by mouse bridge