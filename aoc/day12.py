# ruff: noqa: T201

from aoc.util import get_lines


def num_combos(springs: str, groups: list[int], *, mid_group: bool = False) -> int:
    cur_spring = springs[0]
    rest_springs = springs[1:]
    n_springs = len(springs)

    cur_group = groups[0]
    n_groups = len(groups)

    if cur_spring == ".":
        if n_springs == 1 and n_groups == 1 and cur_group == 0:
            return 1
        if not mid_group:
            return num_combos(rest_springs, groups.copy(), mid_group=False)
        return 0

    if cur_spring == "#":
        if n_springs == 1 and n_groups == 1 and cur_group == 1:
            return 1
        groups[0] -= 1
        if cur_group == 1:
            return num_combos(rest_springs, groups[1:].copy(), mid_group=False)
        return num_combos(rest_springs, groups.copy(), mid_group=True)

    take_groups = groups.copy()
    take_groups[0] -= 1
    take = num_combos(rest_springs, take_groups, mid_group=True)

    if (
        n_springs == 1
        and cur == "."
        and not mid_group
        and n_groups == 1
        and groups[0] == 0
    ):
        return 1

    if len(springs) == 1 and springs[0] == "#" and len(groups) == 1 and groups[0] == 1:
        return 1

    if len(springs) == 1 and springs[0] == "?":
        x = 0
        if
        return 1

    return 0


def part_a() -> int:
    lines = get_lines("day12-sample.txt")
    total = 0
    for line in lines:
        springs, groups = line.split()
        groups = [int(x) for x in groups.split(",")]
        total += num_combos(springs, groups)
        print(total)
    return total


if __name__ == "__main__":
    print(part_a())
