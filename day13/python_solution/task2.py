from sys import argv
from answer_submitter import submit_answer
from numpy import array, where


def find_line_of_reflection(pattern):
    top_index = 0
    bottom_index = pattern.shape[0] - 1
    for i in range(1, len(pattern)):
        unequal_rows = []
        above_index = i - 1
        below_index = i
        while above_index >= top_index and below_index <= bottom_index:
            unequal_elements = where(pattern[above_index, :] != pattern[below_index, :])[0]
            if len(unequal_elements) > 0:
                unequal_rows.append(len(unequal_elements))
            above_index -= 1
            below_index += 1
        if len(unequal_rows) == 1 and unequal_rows[0] == 1:
            return i
    return -1


def calculate_pattern_value(pattern):
    index = find_line_of_reflection(pattern)
    direction = "h"
    if index == -1:
        index = find_line_of_reflection(pattern.T)
        direction = "v"
    return (index) * (100 if direction == "h" else 1)


def solve_second_task(data):
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

    solution = solve_second_task(data)
    print(f"Solution to {'first' if part == 'a' else 'second'} task: ", solution)

    data.close()

    if should_submit:
        submit_answer(solution, part, day, 2023)


if __name__ == "__main__":
    main()
