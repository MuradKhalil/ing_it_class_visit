"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from spaceship_titanic.pipelines import data_proc as dp
from spaceship_titanic.pipelines import data_science as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_proc = dp.create_pipeline()
    data_science = ds.create_pipeline()

    return {
        "__default__": data_proc + data_science,
        "dp": data_proc,
        "ds": data_science,
        }
