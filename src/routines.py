from concurrent.futures import thread
from datetime import datetime

from src.cli_types import ProcessStats, RequirementsResults, TestResults
from src.math import process_test_results
import subprocess

from src.parser import CassandraStressParser


def execute_stress_routine(requirements_results: RequirementsResults, host_ip: str):
    threads = requirements_results.number_stress_tests
    test_result_list = []
    with thread.ThreadPoolExecutor(max_workers=threads) as executor:
        for _ in range(threads):
            future = executor.submit(run_stress_test, host_ip)
            test_results, stats = future.result()
            test_result_list.append(test_results)
            requirements_results.process_stats.append(stats)
    process_test_results(test_result_list, requirements_results)


def run_stress_test(host_ip: str) -> tuple[TestResults, ProcessStats]:
    start = datetime.now()
    completed = subprocess.run(
        f"docker run --rm -it --network=host scylladb/cassandra-stress 'cassandra-stress write duration=1s -rate threads=10 -node {host_ip}'",
        shell=True,
        text=True,
        capture_output=True,
    )
    end = datetime.now()
    stats = ProcessStats(start, end, end - start)
    test_results = CassandraStressParser().create_test_results(completed.stdout)
    return (test_results, stats)
