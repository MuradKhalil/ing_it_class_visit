from kedro.pipeline import Pipeline, node
from .nodes import get_shape, split_data, train_model, evaluate_model

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=get_shape,
                inputs=['train'],
                outputs=None,
                name="get_shape_node",
            ),
            node(
                func=split_data,
                inputs=['train'],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=['X_train', 'y_train'],
                outputs='model',
                name='train_model_node'
            ),
            node(
                func=evaluate_model,
                inputs=['model', 'X_test', 'y_test',],
                outputs=None,
                name='evaluate_model_node'
            )
        ]
    )