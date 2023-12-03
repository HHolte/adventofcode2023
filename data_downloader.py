from aocd import get_data
from os import getenv
from dotenv import load_dotenv

load_dotenv()
SESSION_TOKEN = getenv("SESSION_TOKEN")


def download_and_save_data(day: int, year: int):
    data = get_data(SESSION_TOKEN, day, year)
    save_data_to_file(day, data, data)


def save_data_to_file(day: int, example_data, test_data):
    example_file_name = get_file_name(day, "example")
    test_file_name = get_file_name(day, "test")

    example_file = open(example_file_name, "w+")
    test_file = open(test_file_name, "w+")

    example_file.write(example_data)
    test_file.write(test_data)


def get_file_name(day: int, dataset: str):
    return f"day{day}/{dataset}_data.txt"


if __name__ == "__main__":
    download_and_save_data(1, 2023)
