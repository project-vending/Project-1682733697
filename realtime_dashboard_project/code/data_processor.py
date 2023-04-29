python
import pandas as pd
from typing import List
from datetime import datetime


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the streaming data for analysis.

    Args:
    data (pd.DataFrame): The raw streaming data.

    Returns:
    pd.DataFrame: The preprocessed data.
    """
    # Add a timestamp column
    data["timestamp"] = datetime.now()

    # Perform any necessary preprocessing steps on the data, such as cleaning or feature engineering

    return data


def analyze_data(data: pd.DataFrame, analysis_columns: List[str]) -> pd.DataFrame:
    """
    Analyzes the preprocessed streaming data.

    Args:
    data (pd.DataFrame): The preprocessed data.
    analysis_columns (List[str]): The columns to use in the analysis.

    Returns:
    pd.DataFrame: The analyzed data.
    """
    # Perform any necessary analysis on the preprocessed data, such as aggregations or visualizations
    analysis = data[analysis_columns].describe()

    return analysis
