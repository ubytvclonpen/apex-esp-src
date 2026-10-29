"""Visibility / team / distance filters applied before rendering."""
from __future__ import annotations

import math

from apex_esp.core.models.player import PlayerSnapshot, Vec3
from apex_esp.core.models.world import LocalView


def distance(a: Vec3, b: Vec3) -> float:
    return math.dist((a.x, a.y, a.z), (b.x, b.y, b.z))


def keep_player(p: PlayerSnapshot, view: LocalView, local_team: int, max_m: float) -> bool:
    if not p.is_alive:
        return False
    if p.team == local_team:
        return False
    return distance(p.origin, view.origin) <= max_m