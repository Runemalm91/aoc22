#!/usr/bin/env python3
import sys
import copy


def crate_mover_9000(crate_arrangement, instructions):
    for instruction in instructions:
        number_of_pops = instruction[0]
        stack_from = instruction[1]
        stack_to = instruction[2]
        for _ in range(number_of_pops):
            crate_arrangement[stack_to - 1].append(
                crate_arrangement[stack_from - 1].pop()
            )

    return crate_arrangement


def crate_mover_9001(crate_arrangement, instructions):
    for instruction in instructions:
        number_of_pops = instruction[0]
        stack_from = instruction[1]
        stack_to = instruction[2]

        temporary_stack = []
        for _ in range(number_of_pops):
            temporary_stack.append(crate_arrangement[stack_from - 1].pop())
        temporary_stack.reverse()
        crate_arrangement[stack_to - 1].extend(temporary_stack)

    return crate_arrangement


def collect_top_crates(crate_arrangement):
    return "".join([stack[-1] for stack in crate_arrangement if stack])


def get_top_crates(crates):
    with open(crates, "r") as data:
        puzzle_input = data.readlines()

        crate_arrangement = []
        instructions = []
        for line in puzzle_input:
            line = line.rstrip()
            if "[" in line:  # Criterion derived from data inspection
                stack_counter = 0
                i = 1  # Stack 1 always starts on index 1, derived from data inspection
                while i < len(line):
                    if stack_counter >= len(crate_arrangement):
                        crate_arrangement.append([])  # Create another stack
                    if line[i] != " ":
                        crate_arrangement[stack_counter].append(line[i])
                    i = i + 4  # Constant offset, derived from data inspection
                    stack_counter = stack_counter + 1
            elif line.startswith("move"):  # Criterion derived from data inspection
                instructions.append([int(d) for d in line.split() if d.isdigit()])

        for stack in crate_arrangement:
            stack.reverse()  # Use reverse so that we can utilize pop()
        crate_arrangement_copy = copy.deepcopy(
            crate_arrangement
        )  # So that we can run back-to-back
        crate_arrangement_part_1 = crate_mover_9000(crate_arrangement, instructions)
        crate_arrangement_part_2 = crate_mover_9001(
            crate_arrangement_copy, instructions
        )

        return (
            collect_top_crates(crate_arrangement_part_1),
            collect_top_crates(crate_arrangement_part_2),
        )


def main():
    # Test
    (top_crates_part_1, top_crates_part_2) = get_top_crates("test_data/day5.txt")
    assert "CMZ" == top_crates_part_1, f"{top_crates_part_1}"
    assert "MCD" == top_crates_part_2, f"{top_crates_part_2}"
    # Task
    (top_crates_part_1, top_crates_part_2) = get_top_crates("data_input/day5.txt")
    print(f"Part 1: Top crates: {top_crates_part_1}")
    print(f"Part 2: Top crates: {top_crates_part_2}")


if __name__ == "__main__":
    sys.exit(main())
