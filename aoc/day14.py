# ruff: noqa: T201


from collections.abc import Iterator
from typing import TypeVar

from aoc.util import get_fp

T = TypeVar("T")


def transpose(itr: Iterator[str]) -> Iterator[str]:
    return map("".join, zip(*itr, strict=True))


def roll_left(itr: Iterator[str]) -> Iterator[str]:
    ret = itr
    for _ in range(100):
        ret = (e.replace(".O", "O.") for e in ret)
    return ret


def left_load(itr: Iterator[str]) -> int:
    return sum(i * (c == "O") for r in itr for i, c in enumerate(r[::-1], 1))


def part_a() -> int:
    return left_load(roll_left(transpose(get_fp("day14.txt").open())))


def spin_cycle() -> None:
    pass


def part_b() -> int:
    return 0


if __name__ == "__main__":
    assert part_a() == 110565
    print(part_b())
