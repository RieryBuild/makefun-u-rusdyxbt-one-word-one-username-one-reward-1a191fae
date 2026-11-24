"""Write the entrant's own make.fun username, one word, to entry.txt.

The file holds exactly the five letters "riery" with no trailing newline:
the bounty gate counts exact characters (1-30), so a trailing newline
would add a sixth character and must never be written."""

import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("riery")


if __name__ == "__main__":
    main()
