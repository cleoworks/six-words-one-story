"""Print the six-word story stored in story.txt."""

from pathlib import Path


def read_story() -> str:
    return (Path(__file__).parent / "story.txt").read_text(encoding="utf-8").strip()


def main() -> None:
    story = read_story()
    words = story.split()
    assert len(words) == 6, f"the story must be exactly six words, got {len(words)}"
    print(story)


if __name__ == "__main__":
    main()
