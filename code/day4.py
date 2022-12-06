#!/usr/bin/env python3
import sys


def get_elf_assignment(elf_pair):
    elf1, elf2 = elf_pair.rstrip().split(",")
    elf1_min, elf1_max = elf1.split("-")
    elf2_min, elf2_max = elf2.split("-")
    return int(elf1_min), int(elf1_max), int(elf2_min), int(elf2_max)


def compute_complete_overlap(elf_pair):
    (elf1_min, elf1_max, elf2_min, elf2_max) = get_elf_assignment(elf_pair)

    if (elf2_min >= elf1_min and elf2_max <= elf1_max) or (
        elf1_min >= elf2_min and elf1_max <= elf2_max
    ):
        return 1
    return 0


def compute_overlap(elf_pair):
    (elf1_min, elf1_max, elf2_min, elf2_max) = get_elf_assignment(elf_pair)

    if elf1_min == elf2_min:
        return 1
    if elf1_max == elf2_max:
        return 1

    if (elf1_min <= elf2_min and elf1_max >= elf2_min) or (
        elf1_min > elf2_min and elf1_min <= elf2_max
    ):
        return 1
    return 0


def get_overlaps(section_assignments):
    with open(section_assignments, "r") as data:
        elf_pairs = data.readlines()

        return (
            sum(map(compute_complete_overlap, elf_pairs)),
            sum(map(compute_overlap, elf_pairs)),
        )


def main():
    # Test
    (num_complete_overlaps, num_overlaps) = get_overlaps("test_data/day4.txt")
    assert 2 == num_complete_overlaps, f"{num_complete_overlaps}"
    assert 4 == num_overlaps, f"{num_overlaps}"
    # Task
    (num_complete_overlaps, num_overlaps) = get_overlaps("data_input/day4.txt")
    print(f"Part 1: Number of complete overlaps: {num_complete_overlaps}")
    print(f"Part 2: Number of overlaps: {num_overlaps}")


if __name__ == "__main__":
    sys.exit(main())
