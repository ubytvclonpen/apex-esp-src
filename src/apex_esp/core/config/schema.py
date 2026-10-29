"""Typed config model for the ESP / aimbot runtime."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RendererConfig:
    backend: str = "d3d11"
    box_color: tuple[int, int, int, int] = (0, 255, 128, 220)
    skeleton: bool = True
    health_bar: bool = True
    max_distance_m: float = 400.0


@dataclass
class AimbotConfig:
    enabled: bool = True
    fov_px: int = 180
    smoothing: float = 2.4
    bone: str = "head"
    max_speed_px: int = 42


@dataclass
class BridgeConfig:
    process: str = "r5apex.exe"
    poll_hz: int = 240
    backend: str = "usermode"


@dataclass
class EspConfig:
    profile: str = "default"
    tick_interval_ms: int = 4
    renderer: RendererConfig = field(default_factory=RendererConfig)
    aimbot: AimbotConfig = field(default_factory=AimbotConfig)
    bridge: BridgeConfig = field(default_factory=BridgeConfig)