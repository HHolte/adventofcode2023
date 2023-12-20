from sys import argv
from answer_submitter import submit_answer
from numpy import array, where


def get_starting_direction(matrix, starting_index: tuple[int, int]):
    y_start, x_start = starting_index
    # S is along one of the top or bottom edges
    if y_start == 0 or y_start == matrix.shape[0]:
        if x_start == 0:
            return y_start, x_start + 1
        if x_start == matrix.shape[1]:
            return y_start, x_start - 1
        if matrix[y_start, x_start + 1] in ["-", "J", "7"]:
            return y_start, x_start + 1
        else:
            return y_start, x_start - 1

    # S is along one of the side edges
    if x_start == 0 or x_start == matrix.shape[1]:
        if y_start == 0:
            return y_start + 1, x_start
        if y_start == matrix.shape[0]:
            return y_start - 1, x_start
        if matrix[y_start + 1, x_start] in ["|", "L", "J"]:
            return y_start + 1, x_start
        else:
            return y_start - 1, x_start

    # S is in the interior
    if matrix[y_start + 1, x_start] in ["|", "L", "J"]:
        return y_start + 1, x_start
    if matrix[y_start - 1, x_start] in ["|", "7", "F"]:
        return y_start - 1, x_start
    if matrix[y_start, x_start + 1] in ["-", "J", "7"]:
        return y_start, x_start + 1
    if matrix[y_start, x_start - 1] in ["-", "L", "F"]:
        return y_start, x_start - 1


def get_next_index(prev_index: tuple[int, int], current_index: tuple[int, int], element_at_index: str):
    y_out, x_out = current_index
    # Index 0 corresponds to y, index 1 corresponds to x, y increases downwards and x increases to the right
    if element_at_index == "|":
        y_out = y_out + 1 if prev_index[0] < current_index[0] else y_out - 1
    elif element_at_index == "-":
        x_out = x_out + 1 if prev_index[1] < current_index[1] else x_out - 1
    elif element_at_index == "L":
        if prev_index[0] < current_index[0]:
            x_out += 1
        else:
            y_out -= 1
    elif element_at_index == "J":
        if prev_index[0] < current_index[0]:
            x_out -= 1
        else:
            y_out -= 1
    elif element_at_index == "7":
        if prev_index[0] > current_index[0]:
            x_out -= 1
        else:
            y_out += 1
    elif element_at_index == "F":
        if prev_index[0] > current_index[0]:
            x_out += 1
        else:
            y_out += 1
    return y_out, x_out


def solve_second_task(data):
    lists = []
    for line in data:
        lists.append([*line.strip()])
    matrix = array(lists)
    start_index_y, start_index_x = where(matrix == "S")
    start_index_y = start_index_y[0]
    start_index_x = start_index_x[0]
    prev_index = (start_index_y, start_index_x)
    index = get_starting_direction(matrix, prev_index)
    pipeline = []
    pipeline.append(prev_index)
    s_reached = False
    while not s_reached:
        element_at_index = matrix[index]
        next_index = get_next_index(prev_index, index, element_at_index)
        if next_index == (start_index_y, start_index_x):
            s_reached = True
        pipeline.append(index)
        prev_index = index
        index = next_index

    enclosed_elements = 0
    for i in range(matrix.shape[0]):
        in_matrix = False
        for j in range(matrix.shape[1]):
            if (i, j) in pipeline:
                if matrix[i, j] in ["|", "L", "J"]:  # Stole the in ["|", "L", "J"], not sure why it works
                    in_matrix = not in_matrix
            else:
                enclosed_elements += 1 if in_matrix else 0
    return enclosed_elements


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
