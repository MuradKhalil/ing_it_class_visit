from kedro.pipeline import Pipeline, node
from .nodes import split_data, train_model, evaluate_model

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=['example'],
                outputs=['X', 'y'],
                name='split_data_node',
            ),
            node(
                func=train_model,
                inputs=['X', 'y'],
                outputs='model',
                name='train_model_node'
            ),
            node(
                func=evaluate_model,
                inputs=['model', 'X', 'y'],
                outputs=None,
                name='evaluate_model_node'
            )
        ]
    )