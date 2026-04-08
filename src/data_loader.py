import pandas as pd


# -------------------------------
# Load Spotify Dataset
# -------------------------------
def load_spotify_data(path):
    spotify_df = pd.read_csv(path)
    return spotify_df


# -------------------------------
# Load Billboard Dataset
# -------------------------------
def load_billboard_data(path):
    billboard_df = pd.read_csv(path)
    return billboard_df


# -------------------------------
# Preview Data (Optional utility)
# -------------------------------
def preview_data(df, name="Dataset"):
    print(f"\n{name} Preview:")
    print(df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())


# -------------------------------
# Check Missing Values
# -------------------------------
def check_missing_values(df, name="Dataset"):
    print(f"\nMissing Values in {name}:")
    print(df.isnull().sum())


# -------------------------------
# Basic Info
# -------------------------------
def dataset_info(df, name="Dataset"):
    print(f"\n{name} Info:")
    print(df.info())