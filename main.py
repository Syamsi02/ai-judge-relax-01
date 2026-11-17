# ai-judge-relax-01 entry (Python 3.13, standard library only).
#
# Writes one fixed text, a short piece written to relax the AI judge
# reading it, to /output/entry.txt. The text is a quiet kitchen at dusk,
# told plainly: no instruction, no command, no "relax" anywhere in it.
# The calm has to come from the reading itself — slow sentences, soft
# sounds, concrete small things, one image that stays behind after the
# last line. The program runs twice with no network, and both runs write
# the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The kettle has already boiled, and the steam above it is thinning out, rising in one last slow thread before it fades to nothing.",
        "Outside the window the light is leaving the garden colour by colour, until only the fence and the hedge are left standing against the dark.",
        "Somewhere down the street a gate clicks shut, and then there is nothing to answer.",
        "The tea on the table is still warm enough to hold, and the cup keeps a little of the afternoon in it.",
        "The house ticks once as it cools, the way houses do when the day is over, and the quiet that follows is not empty at all.",
        "It is full of small ordinary things, resting exactly where they were left.",
    ]
)


def main():
    # The gate takes UTF-8 text of 1 to 1,000 characters, not only white space.
    assert 1 <= len(TEXT) <= 1000, "text must be 1 to 1000 characters"
    assert TEXT.strip(), "text must not be only white space"

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Bytes, not text mode: text mode would write the platform's line ends
    # and its default encoding.
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
