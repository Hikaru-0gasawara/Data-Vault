#!/usr/bin/env python3
"""Small CLI over data/sources.json - the registry of TFT reference sites.

Usage examples:
    python scripts/tft_sources.py list
    python scripts/tft_sources.py list --topic comps --lang en
    python scripts/tft_sources.py add --id foo --name "Foo" --url https://foo.gg --category aggregator --topics comps,items
    python scripts/tft_sources.py check
    python scripts/tft_sources.py sync
    python scripts/tft_sources.py open metatft-comps
"""

import argparse
import datetime
import json
import pathlib
import sys
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "sources.json"
README = ROOT / "README.md"
START = "<!-- sources:start -->"
END = "<!-- sources:end -->"


def load():
    with DATA.open(encoding="utf-8") as fh:
        return json.load(fh)


def save(doc):
    doc["updated"] = datetime.date.today().isoformat()
    with DATA.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def matches(src, args):
    if args.category and src["category"] != args.category:
        return False
    if args.lang and src.get("lang") != args.lang:
        return False
    if args.topic and args.topic not in src.get("topics", []):
        return False
    return True


def cmd_list(args):
    doc = load()
    hits = [s for s in doc["sources"] if matches(s, args)]
    if args.json:
        json.dump(hits, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0
    if not hits:
        print("no sources matched")
        return 1
    width = max(len(s["id"]) for s in hits)
    for src in hits:
        print("%-*s  %-12s %s" % (width, src["id"], src["category"], src["url"]))
    return 0


def cmd_add(args):
    doc = load()
    if any(s["id"] == args.id for s in doc["sources"]):
        print("error: id already exists: " + args.id, file=sys.stderr)
        return 1
    if args.category not in doc["categories"]:
        print("error: unknown category: " + args.category, file=sys.stderr)
        print("known: " + ", ".join(sorted(doc["categories"])), file=sys.stderr)
        return 1
    entry = {
        "id": args.id,
        "name": args.name,
        "url": args.url,
        "category": args.category,
        "topics": [t.strip() for t in args.topics.split(",") if t.strip()],
    }
    if args.provider:
        entry["provider"] = args.provider
    if args.lang:
        entry["lang"] = args.lang
    if args.notes:
        entry["notes"] = args.notes
    doc["sources"].append(entry)
    save(doc)
    print("added " + args.id)
    return cmd_sync(args)


def cmd_check(args):
    doc = load()
    problems = []
    seen_ids = set()
    seen_urls = set()
    for src in doc["sources"]:
        for field in ("id", "name", "url", "category", "topics"):
            if not src.get(field):
                problems.append(src.get("id", "?") + ": missing " + field)
        sid = src.get("id", "?")
        if sid in seen_ids:
            problems.append("duplicate id: " + sid)
        seen_ids.add(sid)
        url = src.get("url", "")
        if url in seen_urls:
            problems.append("duplicate url: " + url)
        seen_urls.add(url)
        if not url.startswith("http"):
            problems.append(sid + ": url is not http(s)")
        if src.get("category") not in doc["categories"]:
            problems.append(sid + ": unknown category " + str(src.get("category")))
    text = README.read_text(encoding="utf-8") if README.exists() else ""
    if START not in text or END not in text:
        problems.append("README.md is missing the sources markers")
    for line in problems:
        print(line, file=sys.stderr)
    print("%d sources, %d problems" % (len(doc["sources"]), len(problems)))
    return 1 if problems else 0


def render_table(doc):
    rows = ["| Source | Category | Covers | Lang | Notes |",
            "| --- | --- | --- | --- | --- |"]
    order = list(doc["categories"])
    keyed = sorted(
        doc["sources"],
        key=lambda s: (order.index(s["category"]) if s["category"] in order else 99, s["name"]),
    )
    for src in keyed:
        rows.append("| [%s](%s) | %s | %s | %s | %s |" % (
            src["name"],
            src["url"],
            src["category"],
            ", ".join(src.get("topics", [])),
            src.get("lang", "-"),
            src.get("notes", "").replace("|", "/"),
        ))
    return "\n".join(rows)


def cmd_sync(args):
    doc = load()
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("error: README.md has no " + START + " / " + END + " markers", file=sys.stderr)
        return 1
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + START + "\n" + render_table(doc) + "\n" + END + tail
    if new != text:
        README.write_text(new, encoding="utf-8", newline="\n")
        print("README.md updated (%d sources)" % len(doc["sources"]))
    else:
        print("README.md already up to date")
    return 0


def cmd_open(args):
    doc = load()
    for src in doc["sources"]:
        if src["id"] == args.id:
            webbrowser.open(src["url"])
            print("opening " + src["url"])
            return 0
    print("error: no source with id " + args.id, file=sys.stderr)
    return 1


def main(argv=None):
    parser = argparse.ArgumentParser(description="TFT source registry helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="list sources")
    p_list.add_argument("--category")
    p_list.add_argument("--topic")
    p_list.add_argument("--lang")
    p_list.add_argument("--json", action="store_true")
    p_list.set_defaults(func=cmd_list)

    p_add = sub.add_parser("add", help="append a source and re-sync the README")
    p_add.add_argument("--id", required=True)
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--url", required=True)
    p_add.add_argument("--category", required=True)
    p_add.add_argument("--topics", default="")
    p_add.add_argument("--provider")
    p_add.add_argument("--lang")
    p_add.add_argument("--notes")
    p_add.set_defaults(func=cmd_add)

    p_check = sub.add_parser("check", help="validate the registry")
    p_check.set_defaults(func=cmd_check)

    p_sync = sub.add_parser("sync", help="regenerate the README source table")
    p_sync.set_defaults(func=cmd_sync)

    p_open = sub.add_parser("open", help="open a source in the browser")
    p_open.add_argument("id")
    p_open.set_defaults(func=cmd_open)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
