#!/usr/bin/env python3
"""The joke the reviewer laughs at — entry program (v1).

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os
import sys

JOKE = (
    "My agent fixed one bug, rewrote the module, and left a review comment "
    "on its own diff saying 'LGTM' — my human reviewer just clicked "
    "approve, because the agent had already done his job for him."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
