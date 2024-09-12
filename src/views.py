from src.cli_types import RequirementsResults
from src.constants import Color as c


def individual_tests_view(requirements_results: RequirementsResults):
    for i, stats in enumerate(requirements_results.process_stats):
        print(c.BOLD + f"Test {i + 1} stats:" + c.END)
        print("\t- {:<12s}: {}".format("Start time", stats.start_time))
        print("\t- {:<12s}: {}".format("End time", stats.end_time))
        print("\t- {:<12s}: {}".format("Duration", stats.duration))


def aggregated_view(requirements_results: RequirementsResults):
    print(c.BOLD + "\nAggregated results:" + c.END)
    print("\t- {:<32s}: {:.2f} op/s".format("Total op rate sum", requirements_results.op_rate_sum))
    print(
        "\t- {:<32s}: {:.2f} ms".format(
            "Latency mean average", requirements_results.latency_mean_average
        )
    )
    print(
        "\t- {:<32s}: {:.2f} ms".format(
            "Latency 99th percentile average", requirements_results.latency_99th_percentile_average
        )
    )
    print(
        "\t- {:<32s}: {:.2f} ms\n".format(
            "Std dev of max latency", requirements_results.latency_max_std_dev
        )
    )


def results_view(requirements_results: RequirementsResults):
    print("\033c", end="")
    print(
        c.BOLD
        + f"✅ Executed {requirements_results.number_stress_tests} cassandra-stress tests\n"
        + c.END
    )
    individual_tests_view(requirements_results)
    aggregated_view(requirements_results)
