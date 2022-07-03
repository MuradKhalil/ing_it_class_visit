"""
This is a boilerplate pipeline 'data_proc'
generated using Kedro 0.18.1
"""
import pandas as pd
from typing import  Tuple
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def combine_datasets(df1: pd.DataFrame, df2: pd.DataFrame, df3: pd.DataFrame) -> pd.DataFrame:
    df_merged = pd.merge(pd.merge(df1, df2, on="PassengerId"), df3, on="PassengerId")

    return df_merged

def split_into_train_test(data: pd.DataFrame) -> Tuple:
    """Splits data into train and test sets.
    Args:
        data: Data containing features and target.
    Returns:
        Split data.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop("Transported", axis=1),
        data["Transported"],
        test_size=0.2,
        random_state=42,
        )

    return X_train, X_test, y_train, y_test

def one_hot_encoding(data: pd.DataFrame) -> pd.DataFrame:
    cat_cols = ["Name", "HomePlanet", "Cabin", "Destination"]
    one_hot_encodings = pd.get_dummies(data, columns=cat_cols)
    
    return one_hot_encodings

def drop_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    df = data.dropna()

    return df

def scale_numeric_features(data: pd.DataFrame) -> pd.DataFrame:
    scaled_features = data.copy()

    col_names = ['Age', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    features = scaled_features[col_names]

    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)

    scaled_features[col_names] = features

    return scaled_features

def feature_engineering(data: pd.DataFrame) -> Tuple:
    df = drop_missing_values(data)
    df = one_hot_encoding(df)
    X_train, X_test, y_train, y_test = split_into_train_test(df)
    X_train = scale_numeric_features(X_train)
    X_test = scale_numeric_features(X_test)

    return X_train, X_test, y_train, y_test
