"""Pure tests; do not require Ollama or internet."""
import unittest
from tools.benchmark_ollama import calculate_metrics


class BenchmarkMetricsTests(unittest.TestCase):
    def test_nanosecond_conversion(self):
        result = calculate_metrics({"eval_count": 100, "eval_duration": 5_000_000_000,
                                    "total_duration": 6_000_000_000, "response": "ok"})
        self.assertEqual(result["generation_tokens_per_sec"], 20.0)
        self.assertEqual(result["total_seconds"], 6.0)

    def test_empty_or_zero_duration(self):
        result = calculate_metrics({"eval_count": 0, "eval_duration": 0})
        self.assertIsNone(result["generation_tokens_per_sec"])
        self.assertEqual(result["generated_tokens"], 0)


if __name__ == "__main__":
    unittest.main()
