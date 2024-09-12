from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class TestResults:
    op_rate: str  # op/s <<- required
    partition_rate: str  # pk/s
    row_rate: str  # row/s
    latency_mean: str  # ms <<- required
    latency_median: str  # ms
    latency_95th_percentile: str  # ms
    latency_99th_percentile: str  # ms <<- required
    latency_999th_percentile: str  # ms
    latency_max: str  # ms <<- required
    total_partitions: str  # pk
    total_errors: str  # pk
    total_gc_count: str  # pk
    total_gc_memory: str  # KiB
    total_gc_time: str  # seconds
    avg_gc_time: str  # ms
    std_dev_gc_time: str  # ms
    total_operation_time: str  # HH:MM:SS


@dataclass
class ProcessStats:
    start_time: datetime
    end_time: datetime
    duration: datetime


class RequirementsResults:
    number_stress_tests: int
    process_stats: List[ProcessStats]
    op_rate_sum: float
    latency_mean_average: float
    latency_99th_percentile_average: float
    latency_max_std_dev: float

    def __init__(self, n_tests: list) -> None:
        try:
            self.number_stress_tests = n_tests[0]
        except IndexError as exc:
            raise ValueError("The number of stress tests must be provided") from exc
        self.process_stats = []
        self.op_rate_sum = None
        self.latency_mean_average = None
        self.latency_99th_percentile_average = None
        self.latency_max_std_dev = None

    def __repr__(self) -> str:
        return (
            f"RequirementsResults("
            f"number_stress_tests={self.number_stress_tests}, "
            f"process_stats={self.process_stats}, "
            f"op_rate_sum={self.op_rate_sum}, "
            f"latency_mean_average={self.latency_mean_average}, "
            f"latency_99th_percentile_average={self.latency_99th_percentile_average}, "
            f"latency_max_std_dev={self.latency_max_std_dev}"
            f")"
        )
