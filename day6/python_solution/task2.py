from answer_submitter import submit_answer
from day6.python_solution.task1 import get_number_of_ways_to_win


def solve_first_task(data: str):
    times = data.readline().split(":")[1].strip().split(" ")
    distances = data.readline().split(":")[1].strip().split(" ")
    time = int("".join(number for number in times if number != ""))
    distance = int("".join(number for number in distances if number != ""))
    return get_number_of_ways_to_win(time, distance)


def main():
    should_submit = False
    data = open("day6/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution to second task: ", solution)

    data.close()

    if should_submit:
        submit_answer(solution, "b", 6, 2023)


if __name__ == "__main__":
    main()
