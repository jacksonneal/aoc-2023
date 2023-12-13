# ruff: noqa: T201
from functools import cache

from aoc.util import get_lines


def take_miss(groups: list[int], *, mid_group: bool) -> list[int] | None:
    if len(groups) == 0:
        return []
    if groups[0] == 0:
        return groups[1:]
    if mid_group:
        return None
    return groups.copy()


def take_hit(groups: list[int]) -> list[int] | None:
    if len(groups) == 0 or groups[0] == 0:
        return None
    taken = groups.copy()
    taken[0] -= 1
    return taken


@cache
def num_combos(springs: str, groups: list[int], *, mid_group: bool = False) -> int:
    groups = list(groups)

    if len(springs) == 0:
        return 1 if len(groups) == 0 or len(groups) == 1 and groups[0] == 0 else 0

    cur_spring = springs[0]
    rest_springs = springs[1:]

    if cur_spring == ".":
        next_groups = take_miss(groups, mid_group=mid_group)
        if next_groups is None:
            return 0
        return num_combos(rest_springs, tuple(next_groups), mid_group=False)
    if cur_spring == "#":
        next_groups = take_hit(groups)
        if next_groups is None:
            return 0
        return num_combos(rest_springs, tuple(next_groups), mid_group=True)
    if cur_spring == "?":
        hit = 0
        next_groups = take_hit(groups)
        if next_groups is not None:
            hit = num_combos(rest_springs, tuple(next_groups), mid_group=True)

        miss = 0
        next_groups = take_miss(groups, mid_group=mid_group)
        if next_groups is not None:
            miss = num_combos(rest_springs, tuple(next_groups), mid_group=False)

        return hit + miss

    return 1_000_000


def part_a() -> int:
    lines = get_lines("day12.txt")
    total = 0
    for line in lines:
        springs, groups = line.split()
        groups = [int(x) for x in groups.split(",")]
        total += num_combos(springs, tuple(groups))
    return total


def part_b() -> int:
    lines = get_lines("day12.txt")
    total = 0
    for line in lines:
        springs, groups = line.split()
        springs = "?".join([springs] * 5)
        groups = ",".join([groups] * 5)
        print(springs, groups)
        groups = [int(x) for x in groups.split(",")]
        total += num_combos(springs, tuple(groups))
    return total


if __name__ == "__main__":
    # assert part_a() == 7732
    assert part_b() == 4500070301581
