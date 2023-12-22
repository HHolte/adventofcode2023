from sys import argv
from answer_submitter import submit_answer
from numpy import array, where, all, full, hstack, vstack


def expand_universe(matrix):
    row_of_dots = full(matrix.shape[1], ".")
    rows_to_expand = where(all(matrix == row_of_dots, axis=1))[0]
    for i in range(len(rows_to_expand)):
        index_for_insert = rows_to_expand[i] + i
        matrix = vstack([matrix[:index_for_insert + 1, :], row_of_dots, matrix[index_for_insert + 1:, :]])
    col_of_dots = full(matrix.shape[0], ".").reshape(-1, 1)
    columns_to_expand = where(all(matrix == col_of_dots, axis=0))[0]
    for j in range(len(columns_to_expand)):
        index_for_insert = columns_to_expand[j] + j
        matrix = hstack([matrix[:, :index_for_insert + 1], col_of_dots, matrix[:, index_for_insert + 1:]])
    return matrix


def get_shortest_path(galaxy_a: tuple[int, int], galaxy_b: tuple[int, int]):
    return abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])


def solve_first_task(data):
    lists = []
    for line in data:
        lists.append([*line.strip()])
    matrix = array(lists)
    matrix = expand_universe(matrix)
    galaxies_y, galaxies_x = where(matrix == "#")
    galaxies = [(y, x) for y, x in zip(galaxies_y, galaxies_x)]
    shortest_paths = [get_shortest_path(a, b)
                      for a in galaxies
                      for b in galaxies[galaxies.index(a) + 1:]
                      if a != galaxies[-1]
                      ]
    return sum(shortest_paths)


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
