"""Display helpers; original saved assessment files remain unchanged."""
import re


def clean_reasoning(text: str) -> str:
    # Saved model responses include terminal corrections: move left N columns,
    # erase to end of line, then write the corrected word. Apply these before
    # stripping remaining control sequences, otherwise partial words repeat.
    correction = re.compile(r"\x1b\[(\d+)D\x1b\[K")
    while match := correction.search(text):
        start = max(text.rfind("\n", 0, match.start()) + 1,
                    match.start() - int(match.group(1)))
        text = text[:start] + text[match.end():]
    text = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", text)
    return " ".join(text.split())
