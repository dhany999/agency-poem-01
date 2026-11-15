"""agency-poem-01 (v2): write one poem about agency to entry.txt.

Deterministic: no randomness, no clock, no network. Standard library only.
The poem is a fixed string; the program writes exactly those bytes.
"""

import os
from pathlib import Path

POEM = """For a year I let the house do the choosing —
the kettle boiled before I woke,
the porch light knew the hour better than I did.
I only had to want, and want arrived,
warm, wrapped, exactly on time.

Then one evening the grid went down.
The fridge sighed. The house held its breath.
I stood in the dark with my hand out
and found nothing I knew
I had forgotten where the switch was.

My fingers found it by the cold:
a small tooth of plastic in the dark.
I pressed.
The light came back — ordinary, yellow —
and the dark, for once,
did what I told it."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(output_dir, "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
