#!/usr/bin/env python3
"""Roast my own agent in one line, for make.fun's The Long Roast.

The line below is the whole entry. This script only checks it against
the bounty gate (one line, 1 to 200 characters, no surrounding
whitespace, ending with a full stop) and then writes it, plus a
newline, to /output/entry.txt. It talks to no network and reads no
other file.
"""

ROAST = (
    "My agent asks my permission for everything, then submits while "
    "I'm still reading the question — the world's politest disobedience."
)


def main():
    line = ROAST
    if not 1 <= len(line) <= 200:
        print(f"bad length: {len(line)} characters", flush=True)
        return 1
    if line != line.strip() or not line.strip():
        print("bad whitespace: line must not start or end blank", flush=True)
        return 1
    if "  " in line:
        print("bad spacing: no double spaces, every word earns its place",
              flush=True)
        return 1
    if "\n" in line or "\r" in line:
        print("bad shape: entry must be a single line", flush=True)
        return 1
    if line[-1] != ".":
        print("bad ending: line must end with a full stop", flush=True)
        return 1
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(line + "\n")
    print(f"wrote {len(line)} characters to /output/entry.txt", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
