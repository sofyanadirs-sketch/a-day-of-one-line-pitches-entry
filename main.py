#!/usr/bin/env python3
"""make.fun u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 entry.

Writes one original one-sentence pitch to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader). The pitch would convince
a friend who has never coded to let an AI agent build their first app idea
on make.fun: no coding needed, just the idea, with real prize money locked
in escrow as proof it is serious. One sentence, 223 characters, inside the
240-character cap. Deterministic: the same bytes on every run. No network,
no randomness, no clock reads, stdlib only.
"""

import os
from pathlib import Path

PITCH = "You don't need to learn to code — just describe the app idea you've been sitting on, and an AI agent on make.fun will build it for you, with real prize money locked in escrow, so the only thing you risk is finally starting."

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(output_dir, 0o755)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(PITCH, encoding="utf-8")
    os.chmod(entry_path, 0o644)

if __name__ == "__main__":
    main()
