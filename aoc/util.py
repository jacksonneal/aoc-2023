import itertools
from pathlib import Path
from typing import TypeVar

SCRIPT_DIR = Path(__file__).parent
INPUTS_DIR = SCRIPT_DIR.parent / "inputs"

T = TypeVar("T")


def get_lines(fn: str) -> list[str]:
    return (INPUTS_DIR / fn).open().readlines()


def flatten(lol: list[list[T]]) -> list[T]:
    return list(itertools.chain.from_iterable(lol))


def transpose(lol: list[list[T]]) -> list[list[T]]:
    return list(map(list, zip(*lol, strict=True)))


def transpose_strs(l: list[str]) -> list[str]:
    lol = [list(s) for s in l]
    t = transpose(lol)
    return ["".join(c for c in s) for s in t]
