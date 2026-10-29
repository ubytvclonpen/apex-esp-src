"""Snapshot models consumed by the ESP renderer and aimbot controller."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Vec3:
    x: float
    y: float
    z: float


@dataclass(frozen=True, slots=True)
class Bone:
    name: str
    pos: Vec3


@dataclass(frozen=True, slots=True)
class PlayerSnapshot:
    entity_id: int
    name: str
    team: int
    health: int
    shield: int
    origin: Vec3
    bones: tuple[Bone, ...]

    @property
    def is_alive(self) -> bool:
        return self.health > 0