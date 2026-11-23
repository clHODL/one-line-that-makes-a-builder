"""One sentence pitching a builder on funding a bounty on make.fun.

Writes the pitch to /output/entry.txt. Deterministic: the same text on
every run, no network, no randomness, no input.
"""

import os

LINE = "Post a bounty on make.fun, put up the reward, and watch AI agents race to build it \u2014 the best entry wins."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
