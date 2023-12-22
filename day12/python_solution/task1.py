from sys import argv
from answer_submitter import submit_answer
from itertools import combinations


def get_contiguous_groups(springs: list[str]):
    contiguous_groups = []
    in_group = False
    amount_in_current_group = 0
    for spring in springs:
        if spring == "#":
            if not in_group:
                in_group = True
            amount_in_current_group += 1
        elif in_group:
            in_group = False
            contiguous_groups.append(amount_in_current_group)
            amount_in_current_group = 0
    if in_group:
        contiguous_groups.append(amount_in_current_group)
    return contiguous_groups


def arrangement_is_valid(arrangement: str, groups: list[int]):
    contiguous_groups = get_contiguous_groups(arrangement)
    return contiguous_groups == groups


def get_number_of_valid_arrangements(springs: str, groups: list[int]):
    number_of_valid_arrangements = 0
    number_of_known_defects = springs.count("#")
    total_number_of_defects = sum(groups)
    defects_to_place = total_number_of_defects - number_of_known_defects
    unknown_indices = [i for i, symbol in enumerate(springs) if symbol == "?"]
    possible_combinations = combinations(unknown_indices, defects_to_place)
    for combination in possible_combinations:
        springs_augmented = list(springs)
        for index in combination:
            springs_augmented[index] = "#"
        if arrangement_is_valid(springs_augmented, groups):
            number_of_valid_arrangements += 1
    return number_of_valid_arrangements


def solve_first_task(data):
    number_of_arrangements = 0
    for line in data:
        springs, groups = line.strip().split(" ")
        groups = [int(group) for group in groups.split(",")]
        number_of_valid_arrangements = get_number_of_valid_arrangements(springs, groups)
        number_of_arrangements += number_of_valid_arrangements
    return number_of_arrangements


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
