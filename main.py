import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
ENTRY = (
    "My daughter said her friend's dad tells funnier jokes. "
    "I said impossible — I'm the pun-isher in this house.\n"
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
