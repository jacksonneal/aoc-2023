# ruff: noqa: T201
import re
from collections import defaultdict
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


def day2a() -> int:
    n_red_cubes = 12
    n_green_cubes = 13
    n_blue_cubes = 14

    lines = get_lines("day2.txt")

    total = 0
    for line in lines:
        sections = line.strip().split(";")
        sections = sections[0].strip().split(":") + sections[1:]

        game_ok = True
        for section in sections[1:]:
            if not game_ok:
                break
            for cube_count in section.strip().split(","):
                count_and_color = cube_count.strip().split(" ")
                count = int(count_and_color[0])
                color = count_and_color[1]
                if (
                    color == "red"
                    and count > n_red_cubes
                    or color == "green"
                    and count > n_green_cubes
                    or color == "blue"
                    and count > n_blue_cubes
                ):
                    game_ok = False
                    break

        game_num = int(sections[0].split(" ")[1])
        if game_ok:
            total += game_num
    return total


def day2b() -> int:
    total = 0
    lines = get_lines("day2.txt")
    for line in lines:
        min_red = 0
        min_blue = 0
        min_green = 0
        sections = line.strip().split(";")
        sections = [*sections[0].split(":") + sections[1:]]
        for section in sections[1:]:
            for cube_count in section.split(","):
                count_and_color = cube_count.strip().split(" ")
                count = int(count_and_color[0])
                color = count_and_color[1]
                if color == "red":
                    min_red = max(min_red, count)
                elif color == "green":
                    min_green = max(min_green, count)
                elif color == "blue":
                    min_blue = max(min_blue, count)
        total += min_red * min_green * min_blue
    return total


def day3a() -> int:
    lines = get_lines("day3.txt")

    n_map: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    s_map: dict[int, list[int]] = defaultdict(list)

    for i, ln in enumerate(lines):
        line = ln.strip()
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            n_map[i].append((number.start(0), number.end(0), int(number.group(0))))
        symbols = re.finditer(r"[^\d.]", line)
        for symbol in symbols:
            s_map[i].append(symbol.start(0))

    total = 0
    for row in n_map:
        for start, end, number in n_map[row]:
            for i in range(start, end):
                if (
                    i == start
                    and (
                        i - 1 in s_map[row - 1]
                        or i - 1 in s_map[row]
                        or i - 1 in s_map[row + 1]
                    )
                    or i in s_map[row - 1]
                    or i in s_map[row + 1]
                    or i == end - 1
                    and (
                        i + 1 in s_map[row - 1]
                        or i + 1 in s_map[row]
                        or i + 1 in s_map[row + 1]
                    )
                ):
                    total += number
    return total


def day3b() -> int:
    lines = get_lines("day3.txt")

    n_map: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for i, ln in enumerate(lines):
        line = ln.strip()
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            n_map[i].append((number.start(0), number.end(0), int(number.group(0))))

    def get_digit(i: int, j: int) -> tuple[int, int, int] | None:
        for start, end, number in n_map[i]:
            if start <= j < end:
                return start, end, number
        return None

    def get_digits_around(i: int, j: int) -> list[int]:
        digits: set[tuple[int, int, int]] = set()
        for x, y in [
            (i - 1, j - 1),
            (i, j - 1),
            (i + 1, j - 1),
            (i - 1, j),
            (i, j),
            (i + 1, j),
            (i - 1, j + 1),
            (i, j + 1),
            (i + 1, j + 1),
        ]:
            digit = get_digit(x, y)
            if digit is not None:
                digits.add(digit)
        return [y[2] for y in digits]

    total = 0
    for i, ln in enumerate(lines):
        line = ln.strip()
        for j, char in enumerate(line):
            if char == "*":
                digits = get_digits_around(i, j)
                if len(digits) == 2:
                    total += digits[0] * digits[1]

    return total


def day4a() -> int:
    lines = get_lines("day4.txt")
    total = 0

    for line in lines:
        winning_numbers: list[int] = []
        my_numbers: list[int] = []
        i = 0
        for match in re.finditer(r"\d+\s", line):
            if i < 10:
                winning_numbers.append(int(match.group(0)))
            else:
                my_numbers.append(int(match.group(0)))
            i += 1

        num_winning = 0
        for n in my_numbers:
            if n in winning_numbers:
                num_winning += 1
        if num_winning > 0:
            total += 2 ** (num_winning - 1)

    return int(total)


def day4b() -> int:
    lines = get_lines("day4.txt")

    total = 0
    copies: dict[int, int] = defaultdict(lambda: 1)

    for li, line in enumerate(lines):
        winning_numbers: list[int] = []
        my_numbers: list[int] = []
        i = 0
        for match in re.finditer(r"\d+\s", line):
            if i < 10:
                winning_numbers.append(int(match.group(0)))
            else:
                my_numbers.append(int(match.group(0)))
            i += 1

        num_winning = 0
        for n in my_numbers:
            if n in winning_numbers:
                num_winning += 1

        for _ in range(copies[li]):
            total += 1
            for ni in range(1, num_winning + 1):
                copies[li + ni] += 1

    return int(total)


if __name__ == "__main__":
    # assert day1a() == 54159
    # assert day1b() == 53866

    # assert day2a() == 2679
    # assert day2b() == 77607

    # assert day3a() == 556057
    # assert day3b() == 82824352

    # assert day4a() == 20407
    # assert day4b() == 23806951
    pass
