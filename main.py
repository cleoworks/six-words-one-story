"""Print the six-word story stored in story.txt, verifying its word count."""

import sys
from pathlib import Path


def read_story() -> str:
    path = Path(__file__).parent / "story.txt"
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        print("story.txt is missing next to main.py", file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    story = read_story()
    words = story.split()
    if len(words) != 6:
        print(f"the story must be exactly six words, got {len(words)}", file=sys.stderr)
        raise SystemExit(1)
    if not story.endswith("."):
        print("the story must end with a period", file=sys.stderr)
        raise SystemExit(1)
    print(story)


if __name__ == "__main__":
    main()
