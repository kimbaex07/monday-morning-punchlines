"""Monday Morning Punchlines — make.fun entry.

Writes a single original one-line joke about Monday mornings to
``entry.txt`` inside the output directory given by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``).
Pure Python standard library only; deterministic; no network access.
"""

import os

LINE = "Monday morning is the only time my bed files for custody of me."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
