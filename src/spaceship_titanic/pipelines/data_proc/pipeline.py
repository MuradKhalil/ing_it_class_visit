"""
This is a boilerplate pipeline 'data_proc'
generated using Kedro 0.18.1
"""
from kedro.pipeline import Pipeline, node
from sqlalchemy import func
from .nodes import feature_engineering, combine_datasets

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=combine_datasets,
                inputs=['train1', 'train2', 'train3'],
                outputs='combined_data',
                name='combine_data_node',
            ),
            node(
                func=feature_engineering,
                inputs=['combined_data'],
                outputs=['X_train', 'X_test', 'y_train', 'y_test'],
                name='feature_engineering_node',
            ),
        ]
    )