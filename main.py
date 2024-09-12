import argparse
import logging
import threading

from src.routines import execute_stress_routine
from src.spinner import SpinnerThread
from src.cli_types import RequirementsResults
from src.views import results_view
from src.constants import Color as c, HOST_IP, DEFAULT_HOST_IP


def _check_env_vars_set():
    """Check if the required environment variables are set."""
    if HOST_IP == DEFAULT_HOST_IP:
        logging.warning(
            c.YELLOW
            + f"The `HOST_IP` environment variable is not set, defaulting to: {HOST_IP}"
            + c.END,
        )


def _set_parser() -> argparse.ArgumentParser:
    """Set the command line parser interface."""
    parser = argparse.ArgumentParser(
        prog="Cassandra stress test",
        description="Run N cuncurrent cassandra-stress test commands",
    )
    parser.add_argument(
        "n_stress_tests",
        metavar="N",
        type=int,
        nargs=1,
        help="The number of cassandra-stress tests to run",
        choices=range(1, 11),  # limit to 10 tests max
        action="store",
    )
    return parser.parse_args()


def _run_cli(args):
    requirements_results = RequirementsResults(args.n_stress_tests)
    task = threading.Thread(
        target=execute_stress_routine,
        args=(requirements_results, HOST_IP),
    )
    print(
        f"Running {requirements_results.number_stress_tests} cassandra-stress tests, please wait..."
    )
    task.start()
    spinner_thread = SpinnerThread()
    spinner_thread.start()
    task.join()
    spinner_thread.stop()
    results_view(requirements_results)


def main():
    _check_env_vars_set()
    args = _set_parser()
    _run_cli(args)


if __name__ == "__main__":
    main()
