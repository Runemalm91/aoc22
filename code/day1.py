#!/usr/bin/env python3
import sys


def get_calories_per_elf():
    with open("data_input/day1.txt", "r") as data:
        calories = data.readlines()
        calories_per_elf = []
        calory_sum = 0
        for calory in calories:
            if calory == "\n":
                calories_per_elf.append(calory_sum)
                calory_sum = 0
                continue
            calory_sum += int(calory)
    return calories_per_elf


def part_one(calories_per_elf):
    print(f"Part 1: Max number of calories {max(calories_per_elf)}")


def part_two(calories_per_elf):
    calories_per_elf.sort(reverse=True)
    print(
        f"Part 2: Total number of calories carried by top 3 elves: {sum(calories_per_elf[0:3])}"
    )


def main():
    calories_per_elf = get_calories_per_elf()
    part_one(calories_per_elf)
    part_two(calories_per_elf)


if __name__ == "__main__":
    sys.exit(main())
