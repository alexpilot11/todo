import subprocess
import sys
import time

SLEEP = 10


def check_db_ready(*args):
    retries = 6

    rc = None
    args = ["pg_isready", "-p", "5433"] + list(args)
    print("Checking readiness with", " ".join(args))

    while rc != 0 and retries:
        print(f"...waiting {SLEEP}s before checking database")
        time.sleep(SLEEP)
        rc = subprocess.call(args)
        retries -= 1

    return rc


if __name__ == "__main__":
    print("CHECK", " ".join(sys.argv[1:]))
    check_type = sys.argv[1]

    rc = 1

    if check_type == "db_ready":
        rc = check_db_ready(*sys.argv[2:])
    else:
        print(f"Don't know how to check {check_type}")

    sys.exit(rc)

