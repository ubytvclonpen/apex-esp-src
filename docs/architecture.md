# apex-esp-src architecture

The overlay runs as a separate Windows process and talks to the game through
`src/apex_esp/infra/driver_bridge.py`. Feature modules live under
`src/apex_esp/features/`:

- **esp/** — d3d11 overlay renderer, skeleton + box drawing, distance filters
- **aimbot/** — FOV gated controller, smoothing, bone targeting

Config is TOML under `config/`. The `scripts/` folder holds build + signing
helpers. `installer/setup.iss` produces the end-user installer.