from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUTS_DIR = SCRIPT_DIR.parent / "inputs"


def get_lines(fn: str) -> list[str]:
    return (INPUTS_DIR / fn).open().readlines()
