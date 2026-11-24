"""Write the entrant's own make.fun username, one word, to entry.txt."""

import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("riery")


if __name__ == "__main__":
    main()
