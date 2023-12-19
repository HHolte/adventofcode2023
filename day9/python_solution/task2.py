from sys import argv
from answer_submitter import submit_answer
from numpy import array, append, diff, all


def solve_second_task(data):
    summ = 0
    for line in data:
        edge_values = array([])
        finished = False
        numbers = array([int(number) for number in line.strip().split(" ")])
        edge_values = append(edge_values, numbers[0])
        while not finished:
            numbers = diff(numbers)
            finished = all(numbers == 0)
            edge_values = append(edge_values, numbers[0])
        new_value = 0
        for value in edge_values[::-1]:
            new_value = value - new_value
        summ += new_value
    return int(summ)


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
