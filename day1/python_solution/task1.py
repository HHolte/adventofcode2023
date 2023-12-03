from answer_submitter import submit_answer


def solve_first_task(file):
    summ = 0
    for line in file:
        number = ""
        for value in line:
            if value.isdigit():
                number += value
                break
        for value in line[::-1]:
            if value.isdigit():
                number += value
                break
        summ += int(number)
    return summ


def main():
    should_submit = False
    data = open("day1/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()

    if should_submit:
        submit_answer(solution, "a", day=1, year=2023)


if __name__ == "__main__":
    main()
