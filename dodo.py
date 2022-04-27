

# pydoit configuration
DOIT_CONFIG = {
    "backend": "sqlite3",
    "verbosity": 2,
    "par_type": "thread"  # avoid trouble with non-linux systems
}


def task_db():
    """
    Perform all db tasks

        1. Initialize the database tablespace

        2. Start the db

        3. Check if the db is ready to accept connections

        4. Create dev and test databases

        5. Execute scripts to create tables

        6.
    """

    yield dict(
        name="db:init",
        doc="Initialize db tablespace",
        actions=[
            "rm -rf data/pg",
            "initdb -D data/pg"
        ]
    )

    yield dict(
        name="db:start",
        doc="Start the db in a background process",
        actions=[
            "pg_ctl -o \"-p 5433\" start -D data/pg"
        ]
    )

    yield dict(
        name="db:check",
        doc="Check if db is ready to accept connections",
        actions=[
            "python -m scripts.check db_ready"
        ]
    )

    yield dict(
        name="db:setup",
        doc="Create dev db",
        actions=[
            "createdb -E UTF8 -T template0 -p 5433 flint_dev",
            "createdb -E UTF8 -T template0 -p 5433 flint_test",
            "psql -p 5433 -d flint_dev -f sql/00_create_databases.sql"
        ]
    )

    yield dict(
        name="db:check:migrations",
        doc="Initialize db tablespace",
        actions=[
            "psql -p 5433 -d flint_dev -f sql/2.0/DDL/create_todo_table_2.0.sql",
            "psql -p 5433 -d flint_dev -f sql/2.0/DML/insert_todos_2.0.sql"
        ]
    )

    yield dict(
        name="db:grant",
        doc="Grant permissions",
        actions=[
            "psql -p $QUARTZ_PG_PORT -d flint_dev -f sql/01_grant_user_perms.sql"
        ]
    )

    yield dict(
        name="db:teardown",
        doc="Cleanup",
        actions=[
            "pg_ctl stop -D data/pg"
        ]
    )


# def task_start_db():
#     yield dict(
#         name="db:"
#     )


def task_unit_tests():

    test_cmd = ["pytest"]

    yield dict(
        name="test",
        doc="Run unit tests",
        actions=test_cmd,
    )


def task_server():
    cmd = ["uvicorn main:app --reload"]
    yield dict(
        name="server",
        doc="Run server",
        actions=cmd,
    )


if __name__ == '__main__':
    import doit
    doit.run(globals())
