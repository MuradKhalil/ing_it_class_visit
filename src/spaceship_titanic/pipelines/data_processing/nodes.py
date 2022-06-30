import pandas as pd
import logging
from typing import  Tuple
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



def get_shape(df: pd.DataFrame):
    """logs shape of the input data
    Args:
        df: input data
    """
    logger = logging.getLogger(__name__)
    logger.info("Shape of the input data is %s.", df.shape)

def split_data(data: pd.DataFrame) -> Tuple:
    """Splits data into features and targets training and test sets.
    Args:
        data: Data containing features and target.
    Returns:
        Split data.
    """
    data = data[['Age', 'Transported']]
    data = data.dropna()
    X = data[['Age']]
    y = data['Transported']
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LogisticRegression:
    """Trains the linear regression model.
    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.
    Returns:
        Trained model.
    """
    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)
    return regressor

def evaluate_model(regressor: LogisticRegression, X_test: pd.DataFrame, y_test: pd.Series):
    """Calculates and logs the coefficient of determination.
    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred = regressor.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has an accuracy of %.3f on test data.", score)