"""agency-poem-01: write one poem about agency to entry.txt.

Deterministic: no randomness, no clock, no network. Standard library only.
The poem is a fixed string; the program writes exactly those bytes.
"""

import os
from pathlib import Path

POEM = """I built a machine that says yes,
so I could finally learn to say no.
It writes the letters, keeps the lists,
answers in my voice, on my behalf —
and every yes it gives away
is one I no longer have to spend.

What I did not expect:
the choosing did not get lighter —
it got heavier. Sharper. Mine.
Each instruction a small door
I open once and cannot unopen.

Agency was never the doing.
The doing was always the easy part.
It is the pause before I ask,
the hand still hovering over the key —
the moment you could walk away,
and the fact that you stay."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(output_dir, "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
