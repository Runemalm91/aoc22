#!/usr/bin/env python3
import sys

MAPPING = {"X": "A", "Y": "B", "Z": "C"}

WIN = 6
DRAW = 3


def calculate_score_part_one(opponent, you):
    if opponent - you == 0:
        return DRAW + you
    if opponent - you == -1 or opponent - you == 2:
        return WIN + you
    return you


def calculate_score_part_two(opponent, outcome):
    if outcome == 2:
        return DRAW + opponent
    if outcome == 1:
        return (opponent + 2) % 3 if (opponent + 2) % 3 else 3
    return WIN + (opponent + 1) % 3 if (opponent + 1) % 3 else WIN + 3


def get_scores():
    # Conversion strategy
    # Convert my X-Y-Z to A-B-C
    # Convert letters to numbers using ascii decoding
    # Use math to find out who wins

    scores1 = []
    scores2 = []
    with open("data_input/day2.txt", "r") as data:
        strategy = data.readlines()
        for outcome in strategy:
            opponent = ord(outcome[0]) - ord("A") + 1
            you = ord(MAPPING[outcome[2]]) - ord("A") + 1
            scores1.append(calculate_score_part_one(opponent, you))
            scores2.append(calculate_score_part_two(opponent, you))

    return scores1, scores2


def main():
    scores1, scores2 = get_scores()
    print(f"Part 1: Total score {sum(scores1)}")
    print(f"Part 2: Total score {sum(scores2)}")


if __name__ == "__main__":
    sys.exit(main())
