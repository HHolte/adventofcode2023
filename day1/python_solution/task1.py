def get_file(filename: str):
    f = open(filename, "r")
    return f


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
    data = get_file("day1/test_data.txt")
    solution = solve_first_task(data)

    print("Solution first task: ", solution)


if __name__ == "__main__":
    main()
