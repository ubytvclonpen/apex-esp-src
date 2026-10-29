# Security policy

`apex-esp-src` is a **game modding / reverse-engineering research project**.
It is distributed as-is, for educational use only.

## Reporting

- Do **not** open public issues for anti-cheat bypass techniques or driver
  vulnerabilities that could affect other users.
- Email `security@apex-esp-src.invalid` with a PGP key request and a short
  repro. We aim to respond within 7 days.

## Scope

- In scope: `src/apex_esp/infra/memory_reader.py`, `overlay/hook.py`,
  `scripts/sign_driver.ps1`.
- Out of scope: bans issued by anti-cheat vendors, third-party loaders.

## Known limitations

- Usermode reads are detected by some anti-cheats; the km driver under
  `installer/` is unsigned by default and will require a test-signing boot
  configuration. You are responsible for how you use it.

## Disclaimer

Using this code in a live match may violate the game's Terms of Service.
The maintainers accept no responsibility for account bans or other
consequences.