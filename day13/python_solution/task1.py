from sys import argv
from answer_submitter import submit_answer
from numpy import array, all


def find_line_of_reflection(pattern):
    prev_row = pattern[0, :]
    top_index = 0
    bottom_index = pattern.shape[0] - 1
    for i in range(1, len(pattern)):
        current_row = pattern[i, :]
        if all(current_row == prev_row):
            above_index = i - 2
            below_index = i + 1
            equal = True
            while equal and above_index >= top_index and below_index <= bottom_index:
                if not all(pattern[above_index, :] == pattern[below_index, :]):
                    equal = False
                above_index -= 1
                below_index += 1
            if equal:
                return i
        prev_row = current_row
    return -1


def calculate_pattern_value(pattern):
    index = find_line_of_reflection(pattern)
    direction = "h"
    if index == -1:
        index = find_line_of_reflection(pattern.T)
        direction = "v"
    return (index) * (100 if direction == "h" else 1)


def solve_first_task(data):
    patterns = []
    current_pattern = []
    for line in data:
        line = line.strip()
        if len(line) == 0:
            patterns.append(array(current_pattern))
            current_pattern = []
        else:
            current_pattern.append([*line])
    patterns.append(array(current_pattern))
    summ = sum([calculate_pattern_value(pattern) for pattern in patterns])
    return summ


def main():
    day = int(argv[1])
    part = argv[2]
    should_submit = argv[3] == "True"

    data = open(f"day{day}/test_data.txt", "r")

    solution = solve_first_task(data)
    print(f"Solution to {'first' if part == 'a' else 'second'} task: ", solution)

    data.close()

    if should_submit:
        submit_answer(solution, part, day, 2023)


if __name__ == "__main__":
    main()
