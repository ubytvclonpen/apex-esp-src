from pathlib import Path

from apex_esp.core.config.loader import load_config


def test_defaults_when_missing(tmp_path: Path):
    cfg = load_config(str(tmp_path / "nope.toml"))
    assert cfg.renderer.backend == "d3d11"
    assert cfg.aimbot.bone == "head"


def test_override(tmp_path: Path):
    p = tmp_path / "esp.toml"
    p.write_text('[aimbot]\nbone = "neck"\nsmoothing = 1.5\n')
    cfg = load_config(str(p))
    assert cfg.aimbot.bone == "neck"
    assert cfg.aimbot.smoothing == 1.5