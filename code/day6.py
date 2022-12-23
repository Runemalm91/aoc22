#!/usr/bin/env python3
import sys


def get_index_for_start_of_package(message, offset):
    for i in range(len(message)):
        if len(set(message[i : i + offset])) == offset:
            return i + offset


def main():
    # Test part 1
    test_index_1 = get_index_for_start_of_package("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
    assert 7 == test_index_1, f"{test_index_1}"
    test_index_2 = get_index_for_start_of_package("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
    assert 5 == test_index_2, f"{test_index_2}"
    test_index_3 = get_index_for_start_of_package("nppdvjthqldpwncqszvftbrmjlhg", 4)
    assert 6 == test_index_3, f"{test_index_3}"
    test_index_4 = get_index_for_start_of_package(
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4
    )
    assert 10 == test_index_4, f"{test_index_4}"
    test_index_5 = get_index_for_start_of_package("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)
    assert 11 == test_index_5, f"{test_index_5}"
    # Task part 1
    with open("data_input/day6.txt", "r") as data:
        message = data.readlines()[0].rstrip()
        index = get_index_for_start_of_package(message, 4)
        print(f"Part 1: Index: {index}")
    # Test part 2
    test_index_1 = get_index_for_start_of_package("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
    assert 19 == test_index_1, f"{test_index_1}"
    test_index_2 = get_index_for_start_of_package("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
    assert 23 == test_index_2, f"{test_index_2}"
    test_index_3 = get_index_for_start_of_package("nppdvjthqldpwncqszvftbrmjlhg", 14)
    assert 23 == test_index_3, f"{test_index_3}"
    test_index_4 = get_index_for_start_of_package(
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14
    )
    assert 29 == test_index_4, f"{test_index_4}"
    test_index_5 = get_index_for_start_of_package(
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14
    )
    assert 26 == test_index_5, f"{test_index_5}"
    # Task part 2
    with open("data_input/day6.txt", "r") as data:
        message = data.readlines()[0].rstrip()
        index = get_index_for_start_of_package(message, 14)
        print(f"Part 2: Index: {index}")


if __name__ == "__main__":
    sys.exit(main())
