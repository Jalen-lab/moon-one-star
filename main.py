#!/usr/bin/env python3
"""The Moon Gets One Star.

The bounty asks for one line, at most 120 characters: the funniest
one-star review of the Moon. A model judge compares entries two at a
time on the brief sealed with the bounty. The brief weighs, in order:
the line is a one-star review of the Moon itself, not of a trip or a
person; it is the funnier of the two, the bigger and quicker laugh
winning on first read; it reads like a real review, with a rating or a
grievance a genuine reviewer would leave; it finds a specific,
surprising grievance about the Moon instead of the obvious jokes about
craters, cheese or how bright it is; and it uses its few characters
well, every word earning its place and the punchline landing before
the limit. A line that would work as a review of any product, with the
Moon swapped out, is weaker than one that could only be about the Moon.

The line this program writes is:

    ★☆☆☆☆ Runs the tides, the calendar and my sleep, takes a week
    off every month, and has never answered one email.

Why it is built that way: the stars up front make it read as a real
review before a single word is read, which is what the brief asks a
genuine reviewer to do. Then the grievance is a job description no
other object in the sky could hold: the Moon runs the tides, the
calendar and the reviewer's sleep, it takes a week off every month
when it goes dark, and after all that unpaid overtime it has never
answered one email. The joke is specific to the Moon twice over, the
tides and the monthly disappearance, and the final clause is the
punchline, an unanswered email from a rock that controls the oceans.
It is 112 characters, inside the 120 limit, and nothing in it could be
swapped for another product.

The program does one thing and does it the same way every run: it writes
exactly that line, and nothing else, to entry.txt in the output
directory.
"""

import os

REVIEW = (
    "★☆☆☆☆ Runs the tides, the calendar and my sleep, takes a week "
    "off every month, and has never answered one email."
)


def main() -> None:
    if not 1 <= len(REVIEW) <= 120:
        raise ValueError(f"review must be 1-120 characters, got {len(REVIEW)}")
    if "\n" in REVIEW or "\r" in REVIEW:
        raise ValueError("review must be a single line")
    if not REVIEW.strip():
        raise ValueError("review must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != REVIEW:
        raise ValueError("entry.txt does not match the review after writing")
    print(REVIEW)


if __name__ == "__main__":
    main()
