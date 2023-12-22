from sys import argv
from answer_submitter import submit_answer
from numpy import array, where, all, full


EXPANSION_TERM = 10**6 - 1


def get_rows_and_cols_to_expand(matrix):
    row_of_dots = full(matrix.shape[1], ".")
    rows_to_expand = where(all(matrix == row_of_dots, axis=1))[0]
    col_of_dots = full(matrix.shape[0], ".").reshape(-1, 1)
    columns_to_expand = where(all(matrix == col_of_dots, axis=0))[0]
    return rows_to_expand, columns_to_expand


def get_shortest_path(galaxy_a: tuple[int, int], galaxy_b: tuple[int, int], rows_to_expand, columns_to_expand):
    extra_rows = sum([EXPANSION_TERM for row in rows_to_expand
                      if galaxy_a[0] < row < galaxy_b[0] or galaxy_b[0] < row < galaxy_a[0]])
    extra_columns = sum([EXPANSION_TERM for column in columns_to_expand
                         if galaxy_a[1] < column < galaxy_b[1] or galaxy_b[1] < column < galaxy_a[1]])
    return abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1]) + extra_rows + extra_columns


def solve_first_task(data):
    lists = []
    for line in data:
        lists.append([*line.strip()])
    matrix = array(lists)
    rows_to_expand, columns_to_expand = get_rows_and_cols_to_expand(matrix)
    galaxies_y, galaxies_x = where(matrix == "#")
    galaxies = [(y, x) for y, x in zip(galaxies_y, galaxies_x)]
    shortest_paths = [get_shortest_path(a, b, rows_to_expand, columns_to_expand)
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
