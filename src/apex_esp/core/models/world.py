"""World snapshot container shared between bridge and features."""
from __future__ import annotations

from dataclasses import dataclass, field

from apex_esp.core.models.player import PlayerSnapshot, Vec3


@dataclass(frozen=True, slots=True)
class LocalView:
    origin: Vec3
    yaw: float
    pitch: float
    fov_deg: float


@dataclass(slots=True)
class WorldSnapshot:
    local_view: LocalView
    players: list[PlayerSnapshot] = field(default_factory=list)
    tick: int = 0