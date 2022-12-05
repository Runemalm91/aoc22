#!/usr/bin/env python3
import sys


def get_common_item(rucksack):
    # Split rucksack into two
    # Compare elements and extract common
    compartment_one = rucksack[: int(len(rucksack) / 2)]
    compartment_two = rucksack[int(len(rucksack) / 2) :]
    for item1 in compartment_one:
        for item2 in compartment_two:
            if item1 != item2:
                continue
            return item1


def get_badge(group):
    # Only need to check unique items in each bag
    # Since a badge need to exist in all rucksacks we can simplify the loop logic by using "in"
    group_with_uniques = ["".join(set(rucksack)) for rucksack in group]
    unique_items = group_with_uniques[0]
    for item in unique_items:
        if (item in group_with_uniques[1]) and (item in group_with_uniques[2]):
            return item


def get_priority(item):
    # Utilizie ascii encoding
    if item.islower():
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


def get_sums(input_file_name):
    # Accumulate sum
    sum_part_one = 0
    sum_part_two = 0
    with open(input_file_name, "r") as data:
        rucksacks = data.readlines()

        group = []
        for rucksack in rucksacks:
            common_item = get_common_item(rucksack)
            sum_part_one += get_priority(common_item)

            group.append(rucksack.rstrip())
            if len(group) == 3:
                badge = get_badge(group)
                sum_part_two += get_priority(badge)
                group = []

    return (sum_part_one, sum_part_two)


def main():
    # Test
    (test_sum_one, test_sum_two) = get_sums("test_data/day3.txt")
    assert 157 == test_sum_one, f"{test_sum_one}"
    assert 70 == test_sum_two, f"{test_sum_two}"
    # Task
    (sum_one, sum_two) = get_sums("data_input/day3.txt")
    print(f"Part 1: Priority sum: {sum_one}")
    print(f"Part 2: Priority sum: {sum_two}")


if __name__ == "__main__":
    sys.exit(main())
