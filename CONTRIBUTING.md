# Contributing to apex-esp-src

Thanks for helping out. This project is a **hobbyist ESP / aimbot source for Apex Legends**,
shared for educational and reverse-engineering purposes. Use it at your own risk — running
cheats online can get your account banned.

## Ground rules

- Follow the existing package layout: `src/apex_esp/features/<feature>/` for feature code,
  `src/apex_esp/core/` for shared models/config, `src/apex_esp/infra/` for OS-facing code.
- New config keys go in `src/apex_esp/core/config/schema.py` **and** `config/esp.toml`.
- Signatures of the `DriverBridge` / `MemoryReader` interfaces must stay stable.

## Local dev

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest -q
python -m apex_esp.app.bootstrap
```

## Pull requests

- Keep PRs small and feature-scoped (e.g. "add skeleton bone whitelist").
- Include a test under `tests/` if you touched `core/` or `features/esp/filters.py`.
- Update `docs/offset_reference.md` if you added a memory read.