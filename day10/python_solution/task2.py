from sys import argv
from answer_submitter import submit_answer
from numpy import array, where
from day10.python_solution.task1 import get_starting_direction, get_next_index


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
