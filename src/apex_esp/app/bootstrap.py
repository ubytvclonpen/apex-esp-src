"""Entry point for the apex-esp-src desktop overlay."""
from __future__ import annotations

import logging

from apex_esp.core.config.loader import load_config
from apex_esp.core.orchestrator import OverlayOrchestrator
from apex_esp.infra.runtime import ensure_directx_runtime


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)s %(levelname)s %(message)s")
    log = logging.getLogger("apex_esp.bootstrap")

    cfg = load_config("config/esp.toml")
    log.info("Loaded config profile=%s backend=%s", cfg.profile, cfg.renderer.backend)

    if not ensure_directx_runtime():
        log.error("DirectX runtime missing — install the redistributable before launching")
        return 2

    orchestrator = OverlayOrchestrator(cfg)
    try:
        orchestrator.run()
    except KeyboardInterrupt:
        log.info("shutdown requested")
    finally:
        orchestrator.teardown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())