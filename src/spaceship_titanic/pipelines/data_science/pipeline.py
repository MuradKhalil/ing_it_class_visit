"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""
from kedro.pipeline import Pipeline, node
from sqlalchemy import func
from .nodes import train_model, evaluate_model

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=train_model,
                inputs=['X_train', 'y_train'],
                outputs='model',
                name='train_model_node',
            ),
            node(
                func=evaluate_model,
                inputs=['model', 'X_test', 'y_test'],
                outputs=None,
                name='evaluate_model_node',
            )
        ]
    )