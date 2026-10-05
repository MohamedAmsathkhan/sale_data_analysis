"""
Data Loader Module
------------------
Handles loading datasets, feature engineering (datetime & month extraction),
and preliminary dataset quality inspection.
"""

import os
from typing import Dict, Any
import pandas as pd


def load_dataset(filepath: str = "Sales_Data_Analysis_Full(1).csv") -> pd.DataFrame:
    """
    Loads dataset from CSV file and performs preliminary transformations.
    Searches in current working directory and parent folder if path doesn't exist.
    """
    target_path = filepath
    if not os.path.exists(target_path):
        # Check relative to module's parent directory
        parent_dir_path = os.path.join(os.path.dirname(__file__), "..", filepath)
        if os.path.exists(parent_dir_path):
            target_path = parent_dir_path
        elif os.path.exists(os.path.join("..", filepath)):
            target_path = os.path.join("..", filepath)
        else:
            raise FileNotFoundError(f"Dataset file '{filepath}' not found.")

    df = pd.read_csv(target_path)

    # Perform date conversion & Month extraction
    if "Order_Date" in df.columns:
        df["Order_Date"] = pd.to_datetime(df["Order_Date"])
        df["Month"] = df["Order_Date"].dt.month

    return df


def inspect_data(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Performs data quality checks and returns summary metrics in a dictionary.
    """
    return {
        "head": df.head(),
        "shape": df.shape,
        "dtypes": df.dtypes,
        "columns": df.columns.tolist(),
        "null_counts": df.isnull().sum(),
        "duplicate_count": df.duplicated().sum(),
        "describe": df.describe(),
        "product_counts": df["Product"].value_counts() if "Product" in df.columns else None,
    }


def print_data_inspection(df: pd.DataFrame) -> None:
    """
    Prints a formatted summary of dataset inspection metrics to console.
    """
    inspection = inspect_data(df)
    print("=" * 60)
    print("                DATA INSPECTION & QUALITY REPORT")
    print("=" * 60)
    print("\n--- FIRST 5 ROWS ---")
    print(inspection["head"])
    print(f"\n--- DATASET SHAPE ---: {inspection['shape'][0]} Rows, {inspection['shape'][1]} Columns")
    print("\n--- DATA TYPES ---")
    print(inspection["dtypes"])
    print("\n--- MISSING VALUES ---")
    print(inspection["null_counts"])
    print(f"\n--- DUPLICATE ROWS ---: {inspection['duplicate_count']}")
    print("\n--- PRODUCT COUNTS ---")
    print(inspection["product_counts"])
    print("\n--- DESCRIPTIVE STATISTICS ---")
    print(inspection["describe"])
    print("=" * 60 + "\n")
