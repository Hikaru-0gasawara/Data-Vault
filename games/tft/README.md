# tft

A small, versioned store for the Teamfight Tactics references I actually use:
where the data lives, what each site is good for, and a place to keep my own
per-patch notes.
Part of [Data-Vault](../..) — see [`games/`](..) for the other games.

Everything is driven by one file: [`data/sources.json`](data/sources.json).
The table below is generated from it, so edit the JSON (or use the CLI) and run
`sync` instead of hand-editing the list.

## Sources

<!-- sources:start -->
| Source | Category | Covers | Lang | Notes |
| --- | --- | --- | --- | --- |
| [TFT Index (Tencent)](https://lol.qq.com/tft/#/index) | official | patch-notes, champions, traits, items | zh-CN | Official Chinese TFT portal. Often lists set data before western sites update. |
| [Blitz - Comps](https://blitz.gg/tft/comps) | aggregator | comps | en | Comp stats from the Blitz desktop app/overlay. |
| [BunnyMuffins - Meta](https://bunnymuffins.lol/meta/) | aggregator | comps, meta | en | High-elo focused meta report. |
| [MetaTFT - Comps](https://www.metatft.com/comps) | aggregator | comps | en | Comp stats plus a companion overlay app. |
| [Mobalytics - Team Comps (pt-BR)](https://mobalytics.gg/pt_br/tft/team-comps) | aggregator | comps, guides | pt-BR | Comp guides with positioning and item priority. Swap pt_br for another locale if needed. |
| [TFTactics - Team Comps Tier List](https://tftactics.gg/tierlist/team-comps/) | aggregator | comps, tierlist | en | Curated S/A/B tier list, lighter on raw stats. |
| [Tacter - TFT Meta](https://www.tacter.com/tft/meta) | aggregator | comps, meta | en | Meta snapshot with coaching-oriented comp breakdowns. |
| [Tactics.tools - Augments](https://tactics.tools/augments) | aggregator | augments | en | Augment win/placement stats, filterable by stage and comp. |
| [Tactics.tools - Items](https://tactics.tools/items) | aggregator | items | en | Item stats and best holders per unit. |
| [Tactics.tools - Team Compositions](https://tactics.tools/team-compositions) | aggregator | comps | en | Comp tier list with avg placement, play rate and rank filters. |
| [Community Cheat Sheet (Google Sheets)](https://docs.google.com/spreadsheets/d/1aEP8kev4DdCod_7fW0-_TTNt1Rhpu6QKrS7zjMLOCD4/htmlview#gid=196125882) | community | cheatsheet, comps | en | Shared spreadsheet; the #gid anchor points at a specific tab. |
<!-- sources:end -->

Categories:

- **official** - first-party Riot/Tencent portals (set data, patch notes).
- **aggregator** - stats sites built on ranked match data (comps, augments, items).
- **community** - hand-maintained sheets and cheat sheets.

## Layout

```
data/sources.json         source of truth - every link with category, topics, notes
data/sources.schema.json  JSON Schema describing that file
scripts/tft_sources.py    CLI: list / add / check / sync / open
notes/                    per-patch meta notes (see notes/TEMPLATE.md)
```

## Usage

Requires Python 3.9+ and nothing else - standard library only.

List everything:

```bash
python scripts/tft_sources.py list
```

Filter by topic, category or language:

```bash
python scripts/tft_sources.py list --topic augments
```

Add a new site (appends to the JSON and regenerates the table below):

```bash
python scripts/tft_sources.py add --id lolchess-meta --name "LoLCHESS - Meta" --url https://lolchess.gg/meta --category aggregator --topics comps --lang en
```

Validate the registry (duplicate ids/urls, unknown categories, missing fields):

```bash
python scripts/tft_sources.py check
```

Regenerate the table in this README after editing the JSON by hand:

```bash
python scripts/tft_sources.py sync
```

Open a source in the browser by id:

```bash
python scripts/tft_sources.py open tactics-tools-comps
```

## Patch notes

Copy [`notes/TEMPLATE.md`](notes/TEMPLATE.md) to `notes/<patch>.md` (e.g.
`notes/15.17.md`) and fill it in while you play. Keeping the notes next to the
source list makes it easy to see which site a read came from.
