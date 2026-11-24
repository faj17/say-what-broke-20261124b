"""One-line software error message for the make.fun bounty.

The whole entry is a single line of error copy that tells the user the
brutal truth about what went wrong and makes them laugh: a Friday deploy
broke the login page, the user's password is fine, our code is not, and
the fix is to try again in five minutes. Gate: 1-200 chars, exactly one
line, no leading or trailing whitespace. The script validates the line
and drops it into /output/entry.txt.
"""

from pathlib import Path

# The error line itself: one line, exactly 117 characters.
ERROR_LINE = (
    "We deployed on a Friday and broke the login page. "
    "Your password is fine \u2014 our code is not. "
    "Try again in five minutes."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Validate the error line as-is; raise ValueError on bad input."""
    if line != line.strip():
        raise ValueError(
            "error line must not have leading or trailing whitespace"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("error line must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"error line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("error line must not be only whitespace")
    return line


def main() -> None:
    text = validate(ERROR_LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
