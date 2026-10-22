#!/usr/bin/env python3
"""Copy shared standards files into the places that need a local copy.

Usage:
  python scripts/sync_standards.py          # copy files
  python scripts/sync_standards.py --check  # exit 1 if any copy is out of date
"""
import shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# source (relative to repo root) -> list of destinations
COPIES = {
    "standards/style-guide-rules.md": [
        "skills/content-design-review/style-guide-rules.md",
    ],
}

def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for src, dests in COPIES.items():
        s = ROOT / src
        if not s.exists():
            print(f"MISSING source: {src}")
            return 1
        for d in dests:
            dp = ROOT / d
            same = dp.exists() and dp.read_bytes() == s.read_bytes()
            if same:
                continue
            if check:
                stale.append(d)
            else:
                dp.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(s, dp)
                print(f"copied {src} -> {d}")
    if check and stale:
        print("Out of date (run: python scripts/sync_standards.py):")
        for d in stale:
            print("  -", d)
        return 1
    if check:
        print("All copies are in sync.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
