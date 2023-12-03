from aocd import submit
from os import getenv
from dotenv import load_dotenv


load_dotenv()
SESSION_TOKEN = getenv("SESSION_TOKEN")


def submit_answer(answer, part: str, day: int, year: int):
    submit(answer=answer, part=part, day=day, year=year, session=SESSION_TOKEN)
