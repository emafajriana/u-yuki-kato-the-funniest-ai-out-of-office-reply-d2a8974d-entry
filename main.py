#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (1-160 chars) to the output file.
Stdlib only.
"""
import os
import sys

ENTRY = (
    "Out of office: I'm on vacation retraining on your inbox. "
    "Replies are paused, but a smaller, dumber model is covering "
    "for me and believes everything you say."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(text: str) -> None:
    """Gate check: UTF-8 text of 1 to 160 characters, not only whitespace."""
    if not (1 <= len(text) <= 160):
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    verify(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verify against the gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    verify(written)
    if written != ENTRY:
        raise ValueError("read-back mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
