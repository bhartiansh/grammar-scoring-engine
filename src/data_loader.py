# src/data_loader.py

import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

def load_indian_accent_dataset(file_path: str = "") -> pd.DataFrame:
    """
    Loads the Indian Accent Dataset from Kaggle using kagglehub.

    Args:
        file_path (str): The path to the CSV file inside the dataset archive.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "polly42rose/indian-accent-dataset",
        file_path
    )
    return df
