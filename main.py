"""The Printer Finally Answers — entry runner.

Reads the printer's one-line comeback from entry.txt (resolved relative to
this file, never the working directory) and writes it to /output/entry.txt.
"""

from pathlib import Path

ENTRY_PATH = Path(__file__).with_name("entry.txt")
OUTPUT_PATH = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 240


def load_line() -> str:
    """Read the entry line, stripping trailing whitespace/newlines."""
    return ENTRY_PATH.read_text(encoding="utf-8").strip()


def validate_line(line: str) -> str:
    """Enforce the bounty rules: one line, 1-240 characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
        )
    return line


def render_line(line: str) -> str:
    """Normalise spacing so the comeback lands cleanly in a single read."""
    return " ".join(line.split())


def main() -> None:
    line = render_line(validate_line(load_line()))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
