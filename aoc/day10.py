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
    grid = [x.strip() for x in get_lines("day10-sample.txt")]
    s = find_s(grid)
    _, seen = bfs(grid, s)

    def in_loop(x: int, y: int) -> bool:
        if (x, y) in seen:
            return False

        num_up_xs = 0
        for i in range(x - 1, -1, -1):
            if grid[i][y] in {"-", "F", "7", "J", "L"} and (i, y) in seen:
                num_up_xs += 1
        if num_up_xs % 2 != 0:
            return True

        num_down_xs = 0
        for i in range(x + 1, len(grid)):
            if grid[i][y] in {"-", "J", "L", "F", "7"} and (i, y) in seen:
                num_down_xs += 1
        if num_down_xs % 2 != 0:
            return True

        num_right_xs = 0
        for j in range(y + 1, len(grid[0])):
            if grid[x][j] in {"|", "7", "J", "F", "L"} and (x, j) in seen:
                num_right_xs += 1
        if num_right_xs % 2 != 0:
            return True

        num_left_xs = 0
        for j in range(y - 1, -1, -1):
            if grid[x][j] in {"|", "F", "L", "J", "7"} and (x, j) in seen:
                num_left_xs += 1
        if num_left_xs % 2 != 0:
            return True

        return False

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if in_loop(i, j):
                print("in loop", i, j)
                total += 1

    return total


if __name__ == "__main__":
    # assert part_a() == 6886
    print(part_b())
