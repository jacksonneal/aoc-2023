# ruff: noqa: T201


import re
from collections.abc import Callable
from functools import reduce
from typing import TypeVar

from aoc.util import get_fp

T = TypeVar("T")


def apply_n(fn: Callable[[T], T], init: T, n: int) -> T:
    return reduce(lambda acc, _: fn(acc), range(n), init)


def read_str(fn: str) -> str:
    return get_fp(fn).open().read().replace("\n", " ")


def rotate_r(s: str) -> str:
    return " ".join(map("".join, zip(*(s.split())[::-1], strict=True)))


def roll_l(s: str) -> str:
    return re.sub("[.O]+", lambda m: "".join(sorted(m[0])[::-1]), rotate_r(s))


def load(s: str) -> int:
    return sum(i for r in s.split() for i, c in enumerate(r[::-1], 1) if c == "O")


def part_a() -> int:
    return load(roll_l(apply_n(rotate_r, read_str("day14.txt"), 2)))


def part_b() -> int:
    d = apply_n(rotate_r, read_str("day14.txt"), 2)
    n = 1000000000
    c = {}
    for r in range(n):
        d = apply_n(roll_l, d, 4)
        if s := c.get(d, 0):
            return c[(n - s) % (r - s) + (s - 1)]
        c |= {d: r, r: load(rotate_r(d))}
    return 0


if __name__ == "__main__":
    assert part_a() == 110565
    print(part_b())
