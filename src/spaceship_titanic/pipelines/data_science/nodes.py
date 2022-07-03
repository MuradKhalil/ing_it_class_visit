"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""
import pandas as pd
import logging
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LogisticRegression:
    """Trains a logistic regression model.
    Args:
        X_train: Training data of independent features.
        y_train: Training data for a target variable.
    Returns:
        Trained model.
    """
    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)
    return regressor

def evaluate_model(regressor: LogisticRegression, X_test: pd.DataFrame, y_test: pd.Series):
    """Calculates and logs the evaluation metric.
    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for a target variable.
    """
    y_pred = regressor.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info('Model has an accuracy of %.3f on test data.', score)