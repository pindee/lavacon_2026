#!/usr/bin/env python3
"""Validate the repository. Exits 1 if anything is wrong. Standard library only."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

def err(msg): errors.append(msg)

REQUIRED = [
    "README.md", "VERSION", "CONTRIBUTING.md", "CHANGELOG.md",
    "standards/style-guide-rules.md", "standards/voice-and-tone.md", "standards/checks.json",
    "terms/terms.json", "plugin/manifest.json", "plugin/code.js", "plugin/ui.html",
    "agent/AGENT.md",
]
for f in REQUIRED:
    if not (ROOT / f).exists():
        err(f"missing required file: {f}")

# VERSION
v = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").exists() else ""
if not re.fullmatch(r"\d+\.\d+\.\d+", v):
    err(f"VERSION must look like 1.2.3, found: {v!r}")

def load(path):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as e:
        err(f"{path}: invalid JSON ({e})")
        return None

terms = load("terms/terms.json")
if isinstance(terms, list):
    for i, t in enumerate(terms):
        if not isinstance(t, dict) or not t.get("avoid") or not t.get("use"):
            err(f"terms/terms.json entry {i} needs non-empty 'avoid' and 'use'")
        else:
            try: re.compile(t["avoid"])
            except re.error as e: err(f"terms/terms.json entry {i}: bad pattern ({e})")
elif terms is not None:
    err("terms/terms.json must be a JSON list")

checks = load("standards/checks.json")
if isinstance(checks, dict):
    if not isinstance(checks.get("max_sentence_words"), int):
        err("standards/checks.json: max_sentence_words must be an integer")
    for i, b in enumerate(checks.get("banned_patterns", [])):
        if not b.get("pattern") or not b.get("message"):
            err(f"standards/checks.json banned_patterns[{i}] needs 'pattern' and 'message'")
        else:
            try: re.compile(b["pattern"])
            except re.error as e: err(f"standards/checks.json banned_patterns[{i}]: bad pattern ({e})")

manifest = load("plugin/manifest.json")
if isinstance(manifest, dict):
    for k in ("name", "id", "api", "main", "ui", "editorType"):
        if k not in manifest:
            err(f"plugin/manifest.json missing key: {k}")

# skills must have frontmatter with name and description
for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{skill.relative_to(ROOT)}: missing frontmatter")
        continue
    fm = m.group(1)
    if not re.search(r"^name:", fm, re.M): err(f"{skill.relative_to(ROOT)}: frontmatter missing name")
    if not re.search(r"^description:", fm, re.M): err(f"{skill.relative_to(ROOT)}: frontmatter missing description")

for p in ROOT.rglob("*.md"):
    if ".git" in p.parts: continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"^(<<<<<<<|>>>>>>>)", t, re.M):
        err(f"{p.relative_to(ROOT)}: contains merge conflict markers")

if errors:
    print("Validation failed:")
    for e in errors: print("  -", e)
    sys.exit(1)
print("Validation passed.")
