"""TOML config loader with sane defaults for apex-esp-src."""
from __future__ import annotations

import tomllib
from pathlib import Path

from apex_esp.core.config.schema import (
    AimbotConfig,
    BridgeConfig,
    EspConfig,
    RendererConfig,
)


def _apply(section: dict, model):
    for k, v in section.items():
        if hasattr(model, k):
            setattr(model, k, v)
    return model


def load_config(path: str) -> EspConfig:
    file = Path(path)
    cfg = EspConfig()
    if not file.exists():
        return cfg
    with file.open("rb") as fh:
        data = tomllib.load(fh)
    cfg.profile = data.get("profile", cfg.profile)
    cfg.tick_interval_ms = data.get("tick_interval_ms", cfg.tick_interval_ms)
    if "renderer" in data:
        _apply(data["renderer"], cfg.renderer)
    if "aimbot" in data:
        _apply(data["aimbot"], cfg.aimbot)
    if "bridge" in data:
        _apply(data["bridge"], cfg.bridge)
    return cfg