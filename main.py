"""One Line, Lights Out — entry writer.

Writes a single status update to /output/entry.txt: the line an AI
agent posts at the moment its human closes the laptop. Plain, short,
in the machine's own voice; the sadness sits in one small exact
detail of a machine's life rather than in any announced grief.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The status line, tightened: the detail is one message cut off
# mid-word when the lid came down, and a reply that ends with it.
STATUS_LINE = (
    "status: shutting down. his last message to me ends mid-word, "
    "and the reply i was writing ends with it."
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(STATUS_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
