# ruff: noqa: T201
import itertools

from .util import flatten, get_lines, transpose_strs


def all_dots(s: str) -> bool:
    return all(c == "." for c in s)


def part_a() -> int:
    g = get_lines("day11.txt")
    g = [r.strip() for r in g]

    g = flatten([[r, r] if all_dots(r) else [r] for r in g])
    g = transpose_strs(g)

    g = flatten([[r, r] if all_dots(r) else [r] for r in g])
    g = transpose_strs(g)

    galaxies: list[tuple[int, int]] = []
    for i, r in enumerate(g):
        for j, c in enumerate(r):
            if c == "#":
                galaxies.append((i, j))

    pairs = list(itertools.combinations(galaxies, 2))

    total = 0
    for (x, y), (i, j) in pairs:
        total += abs(x - i) + abs(y - j)

    return total


def part_b() -> int:
    g = get_lines("day11.txt")
    g = [r.strip() for r in g]

    multiplier = 1_000_000

    extra_rows = [i for i in range(len(g)) if all_dots(g[i])]

    gt = transpose_strs(g)
    extra_cols = [i for i in range(len(gt)) if all_dots(gt[i])]

    galaxies: list[tuple[int, int]] = []
    for i, r in enumerate(g):
        for j, c in enumerate(r):
            if c == "#":
                galaxies.append((i, j))

    pairs = list(itertools.combinations(galaxies, 2))

    total = 0
    for (x, y), (i, j) in pairs:
        total += abs(x - i) + abs(y - j)
        for r in extra_rows:
            if min(x, i) < r < max(x, i):
                total += multiplier - 1
        for c in extra_cols:
            if min(y, j) < c < max(y, j):
                total += multiplier - 1

    return total


if __name__ == "__main__":
    # assert part_a() == 9312968
    # assert part_b() == 597714117556
    pass
