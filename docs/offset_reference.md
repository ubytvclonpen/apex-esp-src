# Apex Legends offset reference (2026 season)

Offsets are dumped per patch with the bundled dumper. Do not hardcode — read
from `config/offsets.json` at runtime.

| symbol           | notes                              |
|------------------|------------------------------------|
| local_player     | pointer to local entity            |
| entity_list      | base + stride                      |
| view_matrix      | 4x4 float                          |
| bone_matrix      | per-model                          |

Update cadence: every seasonal patch. Use `scripts/dump_offsets.py` (WIP).