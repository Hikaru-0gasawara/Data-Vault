# games

Everything game-related lives here — one folder per game, each with its own README.

| Folder | Game | What's inside |
|--------|------|---------------|
| [`cs2/`](cs2) | Counter-Strike 2 | `autoexec.cfg` with all binds, plus 6 crosshair presets (`.cfg`) |
| [`tft/`](tft) | Teamfight Tactics | Reference-site registry in JSON, a Python CLI, and per-patch notes |

The two are independent. `cs2/` is plain config files you copy into the game;
`tft/` ships a script (`scripts/tft_sources.py`, Python 3.9+ standard library
only) that lists, validates, and re-syncs the source table in its own README.
