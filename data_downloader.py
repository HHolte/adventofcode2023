from aocd import get_data
from os import getenv, makedirs
from dotenv import load_dotenv

load_dotenv()
SESSION_TOKEN = getenv("SESSION_TOKEN")


def download_and_save_data(day: int, year: int):
    data = get_data(SESSION_TOKEN, day, year)
    save_data_to_file(day, data)


def save_data_to_file(day: int, test_data):
    test_file_name = get_file_name(day, "test")
    makedirs(f"day{day}", exist_ok=True)
    test_file = open(test_file_name, "w+")
    test_file.write(test_data)
    test_file.close()


def get_file_name(day: int, dataset: str):
    return f"day{day}/{dataset}_data.txt"
