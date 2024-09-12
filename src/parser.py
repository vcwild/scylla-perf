from src.cli_types import TestResults
from datetime import datetime


class CassandraStressParser:
    """A parser for the cassandra-stress command output."""

    def parse(self, text):
        return text.split("\n")

    def get_results(self, output) -> list[str]:
        parsed_output = self.parse(output)
        # get list after matching the "Results:" line
        res = parsed_output[parsed_output.index("Results:") + 1 : -3]
        if len(res) == 17:
            return res
        raise ValueError("The output is not in the expected format")

    def create_test_results(self, output) -> TestResults:
        clean_results = []
        results = self.get_results(output)
        for res in results:
            try:
                tidy = res.split(":", 1)[1].strip().split(" ", 1)[0].replace(",", ".")
                if tidy == "NaN":
                    tidy = "0.0"
                if ":" in tidy:
                    tidy = datetime.strptime(tidy, "%H:%M:%S").time()
                else:
                    tidy = float(tidy)
                clean_results.append(tidy)
            except IndexError as exc:
                raise ValueError(f"The test result for `{res}` could not be parsed") from exc
        return TestResults(*clean_results)
