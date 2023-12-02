# ruff: noqa: T201
import re
from pathlib import Path
from typing import TypeVar

SCRIPT_DIR = Path(__file__).parent
INPUTS_DIR = SCRIPT_DIR.parent / "inputs"

T = TypeVar("T")


def ann(x: T | None) -> T:
    assert x is not None
    return x


def get_lines(fn: str) -> list[str]:
    return (INPUTS_DIR / fn).open().readlines()


def day1a() -> int:
    lines = get_lines("day1.txt")
    total = 0
    for line in lines:
        first_digit = int(ann(re.search(r"\d", line)).group())
        last_digit = int(ann(re.search(r"\d", line[::-1])).group())
        total += first_digit * 10 + last_digit
    return total


TEXT_TO_DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def text_to_digit(text: str) -> int:
    return TEXT_TO_DIGIT[text]


def day1b() -> int:
    lines = get_lines("day1.txt")
    total = 0
    for line in lines:
        first_digit = ann(
            re.search(r"\d|one|two|three|four|five|six|seven|eight|nine", line),
        ).group()
        first_digit = (
            int(first_digit) if len(first_digit) == 1 else text_to_digit(first_digit)
        )
        last_digit = ann(
            re.search(
                r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin",
                line[::-1],
            ),
        ).group()
        last_digit = (
            int(last_digit) if len(last_digit) == 1 else text_to_digit(last_digit[::-1])
        )
        total += first_digit * 10 + last_digit
    return total


if __name__ == "__main__":
    assert day1a() == 54159
    assert day1b() == 53866
