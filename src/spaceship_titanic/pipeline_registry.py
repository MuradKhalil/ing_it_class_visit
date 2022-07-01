"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from spaceship_titanic.pipelines import example_pipeline as ep


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    example_pipeline = ep.create_pipeline()

    return {
        "__default__": example_pipeline,
        "dp": example_pipeline,
        }
