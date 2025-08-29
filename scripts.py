# scripts.py

import pandas as pd
import os

def load_data(filename):
    """Load a CSV file from the data folder"""
    filepath = os.path.join("data", filename)
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded '{filename}' successfully.")
        return df
    except FileNotFoundError:
        print(f"File '{filename}' not found in the 'data/' folder.")
        return None

def explore_data(df):
    """Basic exploration: shape, info, and head"""
    print("\n--- Data Overview ---")
    print(f"Shape: {df.shape}")
    print("\nInfo:")
    df.info()
    print("\nFirst 5 rows:")
    print(df.head())

def preprocess_data(df):
    """Placeholder for data cleaning/preprocessing"""
    # Add preprocessing steps here
    return df

if __name__ == "__main__":
    # Replace with your actual filename
    filename = "your_data.csv"

    df = load_data(filename)
    if df is not None:
        explore_data(df)
        df = preprocess_data(df)
