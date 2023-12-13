# ruff: noqa: T201

from .util import get_lines


def find_s(grid: list[str]) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return i, j
    return -1, -1


def bfs(grid: list[str], start: tuple[int, int]) -> tuple[int, set[tuple[int, int]]]:
    distance = 0
    seen: set[tuple[int, int]] = set()
    queue: list[tuple[tuple[int, int], int]] = [(start, 0)]
    while len(queue) != 0:
        cur, d = queue.pop(0)
        if cur not in seen:
            seen.add(cur)
            distance = max(distance, d)
        else:
            continue

        x, y = cur
        # up
        if (
            x > 0
            and grid[x][y] in {"S", "J", "|", "L"}
            and grid[x - 1][y] in {"7", "|", "F"}
        ):
            queue.append(((x - 1, y), d + 1))
        # down
        if (
            x < len(grid) - 1
            and grid[x][y] in {"S", "7", "|", "F"}
            and grid[x + 1][y] in {"J", "|", "L"}
        ):
            queue.append(((x + 1, y), d + 1))
        # right
        if (
            y < len(grid[0]) - 1
            and grid[x][y] in {"S", "L", "-", "F"}
            and grid[x][y + 1] in {"J", "-", "7"}
        ):
            queue.append(((x, y + 1), d + 1))
        # left
        if (
            y > 0
            and grid[x][y] in {"S", "J", "-", "7"}
            and grid[x][y - 1] in {"L", "-", "F"}
        ):
            queue.append(((x, y - 1), d + 1))

    return distance, seen


def part_a() -> int:
    grid = [x.strip() for x in get_lines("day10.txt")]
    s = find_s(grid)
    d, _ = bfs(grid, s)
    return d


def part_b() -> int:
    grid = [x.strip() for x in get_lines("day10.txt")]
    s = find_s(grid)
    _, seen = bfs(grid, s)

    def in_loop(x: int, y: int) -> bool:
        if (x, y) in seen:
            return False

        num_xs = 0
        i, j = x, y
        while i < len(grid) and j < len(grid[0]):
            cur = grid[i][j]
            if (i, j) in seen and cur not in "L7S":
                num_xs += 1
            i += 1
            j += 1

        return num_xs % 2 != 0

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if in_loop(i, j):
                total += 1

    return total


if __name__ == "__main__":
    # assert part_a() == 6886
    # assert part_b() == 371
    pass
