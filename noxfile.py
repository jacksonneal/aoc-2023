import os
import pathlib

import nox

VENV_DIR = pathlib.Path("./.venv").resolve()


@nox.session
def venv(session: nox.Session) -> None:
    """Create a development virtual environment."""
    session.install("virtualenv")
    session.run("virtualenv", os.fsdecode(VENV_DIR), silent=True)
    python = os.fsdecode(VENV_DIR.joinpath("bin/python"))
    session.run(python, "-m", "pip", "install", "-r", "requirements.txt", external=True)
