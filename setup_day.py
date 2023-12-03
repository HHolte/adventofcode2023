from os import makedirs
from data_downloader import download_and_save_data, get_file_name


def setup_folders_and_files(day: int):
    makedirs(f"day{day}/python_solution", exist_ok=True)
    open(f"day{day}/python_solution/task1.py", "w+").close()
    open(f"day{day}/python_solution/task2.py", "w+").close()
    open(get_file_name(day, "example_task1"), "w+").close()
    open(get_file_name(day, "example_task2"), "w+").close()


def main():
    year = 2023
    day = 3
    setup_folders_and_files(day)
    download_and_save_data(day, year)


if __name__ == "__main__":
    main()
