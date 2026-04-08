import pandas as pd

def checking_for_null_values(df):
    null_counts = df.isnull().sum()
    print("Null values in each column:")
    print(null_counts)

def dropping_null_values(df, feauture):
    df = df.dropna(subset=[feauture])
    return df

def removing_duplicates(df):
    df = df.drop_duplicates()
    return df

def correcting_data_types(spotify_df, billboard_df):
    spotify_df['year'] = spotify_df['year'].astype(int)
    billboard_df['date'] = pd.to_datetime(billboard_df['date'])
    billboard_df['rank'] = billboard_df['rank'].astype(int)
    billboard_df['artist'] = billboard_df['artist'].str.replace(r'Featuring\..*', '', regex=True)
    return spotify_df, billboard_df