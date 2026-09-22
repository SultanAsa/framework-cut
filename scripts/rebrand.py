#!/usr/bin/env python3
"""One-shot rebrand of the upstream fork to FrameWork Cut.

Byte-level edits so each file keeps its own line endings. Every replacement is
asserted to have matched, because a silent zero-match rename is how half a
rebrand ships.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = "FrameWork Cut"
BINARY = "frameworkcut"
IDENT = "shop.framework.cut"
REPO = "SultanAsa/framework-cut"

problems = []


def edit(rel, pairs, required=True):
    p = ROOT / rel
    if not p.exists():
        if required:
            problems.append(f"missing: {rel}")
        return
    data = p.read_bytes()
    before = data
    for old, new in pairs:
        ob, nb = old.encode(), new.encode()
        n = data.count(ob)
        if n == 0 and required:
            problems.append(f"{rel}: no match for {old!r}")
            continue
        data = data.replace(ob, nb)
    if data != before:
        p.write_bytes(data)
        print(f"edited {rel}")


# ── The window: title, crash dialog, about line ──────────────────────────
edit("src/crates/concat/ui/app.slint", [('title: "Concat";', f'title: "{PRODUCT}";')])
edit("src/crates/concat/ui/title-bar.slint", [('text: "Concat";', f'text: "{PRODUCT}";')])
edit("src/crates/concat/src/platform.rs", [
    ('format!("Concat could not start.', f'format!("{PRODUCT} could not start.'),
    ('.set_title("Concat")', f'.set_title("{PRODUCT}")'),
])
edit("src/crates/concat/src/sysinfo.rs", [('format!("Concat {}"', f'format!("{PRODUCT} {{}}"')])
edit("src/crates/concat/src/panes/start.rs", [
    ('"Concat"', f'"{PRODUCT}"'),
    ('"Desktop/Concat"', f'"Desktop/{PRODUCT}"'),
])

# ── Host: log banner, app folder, update repo, project messages ──────────
edit("src/crates/concat-host/src/logs.rs", [('"Concat {} ·', f'"{PRODUCT} {{}} ·')])
edit("src/crates/concat-host/src/dirs.rs", [('"app.concat.editor"', f'"{IDENT}"')])
edit("src/crates/concat-host/src/models.rs", [('"jub0t/Concat"', f'"{REPO}"')])
edit("src/crates/concat-host/src/projects.rs", [
    ('"a Concat project already exists at {}"', f'"a {PRODUCT} project already exists at {{}}"'),
    ("is not a Concat project", f"is not a {PRODUCT} project"),
])
edit("src/crates/concat-host/src/session.rs", [
    ("was saved by a newer Concat than this one", f"was saved by a newer {PRODUCT} than this one"),
])

# ── The binary's own name ────────────────────────────────────────────────
edit("src/crates/concat/Cargo.toml", [
    ('name = "concat"\npath = "src/main.rs"', f'name = "{BINARY}"\npath = "src/main.rs"'),
    ('name = "concat"\r\npath = "src/main.rs"', f'name = "{BINARY}"\r\npath = "src/main.rs"'),
], required=False)
edit("src/crates/concat-cli/src/main.rs", [
    ('about = "Concat engine command line"', f'about = "{PRODUCT} engine command line"'),
    ('"Concat API {}', f'"{PRODUCT} API {{}}'),
    ('println!("Concat API {}: gRPC', f'println!("{PRODUCT} API {{}}: gRPC'),
], required=False)

if problems:
    print("\nPROBLEMS:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("\nrebrand pass complete")
