# ruff: noqa: T201

import itertools

from .util import get_lines, transpose_strs


def middle_out(start: int, end: int) -> list[int]:
    ret: list[int] = []
    middle_index = (start + end) // 2
    for i in range(middle_index, start - 1, -1):
        ret.append(i)
        if i != end:
            ret.append(end - (i - start))
    return ret


def is_mirror(g: list[str], i: int) -> bool:
    for d in range(i + 1):
        if i + d + 1 > len(g) - 1:
            continue
        if g[i - d] != g[i + d + 1]:
            return False
    return True


def get_reflection_score(g: list[str]) -> int:
    x = ((i + 1) * 100 for i in middle_out(0, len(g) - 2) if is_mirror(g, i))
    gt = transpose_strs(g)
    y = ((i + 1) for i in middle_out(0, len(gt) - 2) if is_mirror(gt, i))
    return next(
        item
        for pair in itertools.zip_longest(x, y)
        for item in pair
        if item is not None
    )


def part_a() -> int:
    l = get_lines("day13.txt")
    l = [x.strip() for x in l]

    gs: list[list[str]] = []
    cur_g: list[str] = []
    for s in l:
        if not s:
            gs.append(cur_g)
            cur_g = []
        else:
            cur_g.append(s)
    gs.append(cur_g)

    total = 0
    for g in gs:
        total += get_reflection_score(g)

    return total


def part_b() -> int:
    l = get_lines("day13.txt")
    l = [x.strip() for x in l]

    gs: list[list[str]] = []
    cur_g: list[str] = []
    for s in l:
        if not s:
            gs.append(cur_g)
            cur_g = []
        else:
            cur_g.append(s)
    gs.append(cur_g)

    total = 0
    for g in gs:
        original_score = get_reflection_score(g)
        new_score = original_score
        for i in range(len(g)):
            for j in range(len(g[i])):
                if new_score != original_score:
                    continue
                cur = g.copy()
                cur_sl = list(cur[i])
                cur_sl[j] = "#" if cur[i][j] == "." else "#"
                cur[i] = "".join(cur_sl)
                try:
                    new_score = get_reflection_score(cur)
                except:  # noqa: E722
                    print("failed")
        if new_score != original_score:
            total += new_score

    return total


if __name__ == "__main__":
    # assert part_a() == 40006
    assert part_b() == 28627
    # print(part_b())
    #
    # l = get_lines("day13.txt")
    # l = [x.strip() for x in l]
    #
    # gs: list[list[str]] = []
    # cur_g: list[str] = []
    # for s in l:
    #     if not s:
    #         gs.append(cur_g)
    #         cur_g = []
    #     else:
    #         cur_g.append(s)
    # gs.append(cur_g)
    # patterns = gs
    # def diff(p, j):
    #     return sum(sum(a != b for a, b in zip(l[j:], l[j - 1::-1])) for l in p)
    # mirror = lambda p, d: sum(j for j in range(1, len(p[0])) if diff(p, j) == d)
    # summarize = lambda p, d: mirror(p, d) + 100 * mirror([*zip(*p)], d)
    # print(sum(summarize(p, 0) for p in patterns))
    # print(sum(summarize(p, 1) for p in patterns))
