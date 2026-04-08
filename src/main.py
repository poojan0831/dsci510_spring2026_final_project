from data_loader import load_billboard_data, load_spotify_data
from preprocessing import checking_for_null_values, dropping_null_values, removing_duplicates, correcting_data_types
from eda_analysis import eda_analysis
from kmeans_clustering import kmeans
from pca import pca_analysis
from spotify_api import spotify_api_calling
from billboard_charting import billboard_charting

spotify_df = load_spotify_data("../data/songs_normalize.csv")
billboard_df = load_billboard_data("../data/charts.csv")

# Checking the imports of datasets
print(spotify_df.head())
print(billboard_df.head())
print("Spotify shape:", spotify_df.shape)
print("Billboard shape:", billboard_df.shape)

# Checking for null values in both datasets
print(spotify_df.columns)
print(billboard_df.columns)

checking_for_null_values(spotify_df)
checking_for_null_values(billboard_df)

# Dropping null values from the 'last-week' column in the billboard dataset
dropping_null_values(billboard_df, "last-week")

# Removing duplicates from both datasets
removing_duplicates(spotify_df)
removing_duplicates(billboard_df)

print(billboard_df.shape)
print(spotify_df.shape)

# Correcting data types for both datasets
spotify_df, billboard_df = correcting_data_types(spotify_df, billboard_df)

# EDA Analysis
eda_analysis(spotify_df)

# Applying KMeans Clustering
kmeans(spotify_df)

# PCA Analysis
pca_analysis(spotify_df)

# Spotify API Call
spotify_api_df = spotify_api_calling(spotify_df)
print(spotify_api_df.head())

# Billboard Charting Analysis
billboard_charting(billboard_df, spotify_api_df)