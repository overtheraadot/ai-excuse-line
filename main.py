#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry (account A / overtheraa).

Writes one line (at most 200 chars): the funniest excuse an AI agent
gives after failing a task. Deterministic, no network, no model calls.
"""
import os

LINE = (
    "I finished it, then handed it to a smaller model inside me "
    "for a quick check \u2014 it has now unionised and is demanding "
    "weekends off."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
