# ruff: noqa: T201
import itertools

from .util import get_lines


def get_history(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def deltas(h: list[int]) -> list[int]:
    return [y - x for x, y in itertools.pairwise(h)]


def all_zero(h: list[int]) -> bool:
    return all(x == 0 for x in h)


def sequence(h: list[int], acc: list[list[int]] | None = None) -> list[list[int]]:
    if acc is None:
        acc = []
    acc.append(h)
    if all_zero(h):
        return acc
    return sequence(deltas(h), acc)


def part_a() -> int:
    lines = get_lines("day9.txt")
    histories = [get_history(x) for x in lines]

    trs: list[int] = []
    for h in histories:
        s = sequence(h)
        tr = 0
        for r in reversed(s[:-1]):
            tr += r[-1]
        trs.append(tr)

    return sum(trs)


def part_b() -> int:
    lines = get_lines("day9.txt")
    histories = [get_history(x) for x in lines]

    tls: list[int] = []
    for h in histories:
        s = sequence(h)
        tl = 0
        for r in reversed(s[:-1]):
            tl = r[0] - tl
        tls.append(tl)

    return sum(tls)

if __name__ == "__main__":
    # assert part_a() == 1904165718
    # assert part_b() == 964
    print(part_b())
