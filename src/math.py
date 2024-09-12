from src.cli_types import RequirementsResults, TestResults


def calculate_std_dev(values, mean):
    """Calculate standard deviation given a list of values and their mean."""
    squared_diff_sum = sum((x - mean) ** 2 for x in values)
    return (squared_diff_sum / len(values)) ** 0.5


def process_test_results(test_results_list: TestResults, req_res: RequirementsResults):
    op_rate_sum = 0
    latency_mean_sum = 0
    latency_99th_percentile_sum = 0
    latency_max_sum = 0
    latency_max_values = []
    for test_results in test_results_list:
        op_rate_sum += test_results.op_rate
        latency_mean_sum += test_results.latency_mean
        latency_99th_percentile_sum += test_results.latency_99th_percentile
        latency_max_sum += test_results.latency_max
        latency_max_values.append(test_results.latency_max)  # collect max latencies
    req_res.op_rate_sum = op_rate_sum
    req_res.latency_mean_average = latency_mean_sum / req_res.number_stress_tests
    req_res.latency_99th_percentile_average = (
        latency_99th_percentile_sum / req_res.number_stress_tests
    )
    latency_max_average = latency_max_sum / req_res.number_stress_tests
    req_res.latency_max_std_dev = calculate_std_dev(latency_max_values, latency_max_average)
