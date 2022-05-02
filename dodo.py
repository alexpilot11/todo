# pydoit configuration
DOIT_CONFIG = {
    "backend": "sqlite3",
    "verbosity": 2,
    "par_type": "thread",  # avoid trouble with non-linux systems
}

def task_unit_tests():

    test_cmd = ["pytest"]

    yield dict(
        name="test",
        doc="Run unit tests",
        actions=test_cmd,
    )


def task_server():
    cmd = ["uvicorn todo.main:app --reload"]
    yield dict(
        name="server",
        doc="Run server",
        actions=cmd,
    )


if __name__ == "__main__":
    import doit

    doit.run(globals())
