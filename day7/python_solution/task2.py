from answer_submitter import submit_answer
from math import floor
from day7.python_solution.task1 import cardwise_compare_hands


to_value = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 12, "K": 13, "A": 14}


def get_type(hand: str):
    uniques = "".join(set(hand))
    if len(uniques) == 1 or (len(uniques) == 2 and "J" in uniques):
        return 21
    if "J" not in uniques:
        return get_none_five_type(hand)
    hand_without_j = hand.replace("J", "")
    uniques_without_j = "".join(set(hand_without_j))
    number_of_js = 5 - len(hand_without_j)
    highest_number_of_cards = max([hand_without_j.count(char) for char in uniques_without_j])
    if highest_number_of_cards + number_of_js == 4:
        return 20
    if highest_number_of_cards + number_of_js == 3:
        return 19 if (number_of_js == 1 and len(uniques_without_j) == 2) else 18
    return 16


def get_none_five_type(hand: str):
    uniques = "".join(set(hand))
    if len(uniques) == 2:
        temp = hand.replace(uniques[0], "")
        return 20 if len(temp) == 1 or len(temp) == 4 else 19
    if len(uniques) == 3:
        temp = hand.replace(uniques[0], "")
        if len(temp) == 2:
            return 18
        if len(temp) == 3:
            return 17
        temp = temp.replace(uniques[1], "")
        return 18 if len(temp) == 1 or len(temp) == 3 else 17
    if len(uniques) == 4:
        return 16
    return 15


def compare_hands(first_hand: str, second_hand: str):
    first_hand_type = get_type(first_hand)
    second_hand_type = get_type(second_hand)
    if first_hand_type > second_hand_type:
        return True
    if first_hand_type == second_hand_type:
        cardwise_compare_result = cardwise_compare_hands(first_hand, second_hand, to_value)
        return cardwise_compare_result
    return False


def binary_sort_hand_into_list(hand: str, rank_list: list[str]):
    length_of_list = len(rank_list)
    if length_of_list == 0:
        return [hand]
    index = floor(length_of_list / 2)
    value_at_middle = rank_list[index].split(" ")[0]
    if compare_hands(hand.split(" ")[0], value_at_middle):
        if length_of_list == 1:
            rank_list.append(hand)
            return rank_list
        return rank_list[:index + 1] + binary_sort_hand_into_list(hand, rank_list[index + 1:])
    else:
        if length_of_list == 1:
            rank_list.insert(0, hand)
            return rank_list
        return binary_sort_hand_into_list(hand, rank_list[:index]) + rank_list[index:]


def solve_second_task(data):
    rank_list = []
    for line in data:
        hand_and_bid = line.strip()
        rank_list = binary_sort_hand_into_list(hand_and_bid, rank_list)
    out_value = 0
    for i in range(0, len(rank_list)):
        out_value += (i + 1) * int(rank_list[i].split(" ")[1])
    return out_value


def main():
    should_submit = True
    data = open("day7/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution to second task: ", solution)

    data.close()

    if should_submit:
        submit_answer(solution, "b", 7, 2023)


if __name__ == "__main__":
    main()
