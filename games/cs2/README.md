# cs2

Personal **Counter-Strike 2** configuration files: a full `autoexec.cfg` with custom keybinds, buy binds, and game settings, plus a set of swappable crosshair presets.
Part of [Data-Vault](../..) — see [`games/`](..) for the other games.

## What's inside

| File | Description |
|------|-------------|
| [`autoexec.cfg`](autoexec.cfg) | Main config — all keybinds, buy binds, aliases, viewmodel, and game settings |
| [`csr.cfg`](csr.cfg) | White classic-static crosshair (style 4, small gap) |
| [`donk.cfg`](donk.cfg) | Black compact crosshair, donk-inspired |
| [`dotc.cfg`](dotc.cfg) | Cyan dot-only crosshair |
| [`dotg.cfg`](dotg.cfg) | Green dot-only crosshair |
| [`tap.cfg`](tap.cfg) | White T-less crosshair with tight gap (style 5), tuned for tapping |
| [`lol1.cfg`](lol1.cfg) | Meme crosshair — a giant full-screen bar, for fun only |

## Highlights of `autoexec.cfg`

- **Mousewheel + Space jump** — `MWHEELUP`/`MWHEELDOWN` bound to jump for easier bunnyhopping
- **Desubtick jump/crouch aliases** — double-command jump and duck aliases for more consistent movement in CS2's subtick system
- **Fast switch** — hold `Q` to pull out the knife, release to swap back to your last weapon
- **Quick bomb drop** — `H` selects the bomb and drops it in one press
- **Refund all** — `Backspace` sells back every purchase during buy time
- **Net graph on scoreboard** — `TAB` shows FPS/net info together with the scores
- **Buy binds** — arrow keys and `F9`–`F12` for rifles, SMGs, pistols, utility, and armor
- **Viewmodel & sens** — FOV 68 preset with sensitivity 1.25 and zoom ratio 1.0
- Crosshair share codes from pro setups (s1mple, FalleN, and others) kept as comments for quick import

## Installation

1. Copy the `.cfg` files into your CS2 config folder:

   ```
   Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg
   ```

2. `autoexec.cfg` runs automatically on game start. If it doesn't, add this to your Steam launch options:

   ```
   +exec autoexec.cfg
   ```

3. Swap crosshairs anytime from the in-game console:

   ```
   exec tap
   exec donk
   exec dotg
   ```

> **Note:** `autoexec.cfg` starts with `unbindall`, so it replaces *all* of your current binds. Review the binds section before using it, or back up your own config first.
