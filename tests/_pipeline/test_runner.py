import polars as pl

from cell_eval._pipeline._runner import MetricPipeline


def test_get_agg_results_empty_does_not_raise():
    pipeline = MetricPipeline(profile=None)
    agg = pipeline.get_agg_results()
