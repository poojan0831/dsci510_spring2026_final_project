import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def correlation_matrix_for_spotify(spotify):
    plt.figure(figsize=(14, 10))

    corr_matrix = spotify.corr(numeric_only=True)

    sns.heatmap(
        corr_matrix,
        annot=True,          # show values
        fmt=".2f",           # 2 decimal places
        linewidths=0.5       # spacing
    )

    plt.title("Correlation Heatmap", fontsize=16)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig("../results/correlation_heatmap.png")  # Save the figure
    plt.show()

def effects_of_audio_features_on_popularity(spotify):
    corr = spotify.corr(numeric_only=True)['popularity'].drop('popularity')

    # Filter only meaningful correlations
    corr_filtered = corr[abs(corr) > 0].sort_values()

    plt.figure(figsize=(8, 6))
    corr_filtered.plot(kind='barh')  # horizontal = cleaner
    plt.title("Features vs Popularity (Filtered)")
    plt.xlabel("Correlation")
    plt.tight_layout()
    plt.savefig("../results/features_popularity_correlation.png")  # Save the figure
    plt.show()

def features_trends_over_the_year(spotify):
    yearly_avg = spotify.groupby('year').mean(numeric_only=True)

    features = ['danceability', 'energy', 'valence', 'tempo']

    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform(yearly_avg[features])

    scaled_df = pd.DataFrame(scaled_values, columns=features, index=yearly_avg.index)

    plt.figure(figsize=(10,6))
    for col in features:
        plt.plot(scaled_df.index, scaled_df[col], label=col)

    plt.title("Feature Trends Over Years (Normalized)")
    plt.xlabel("Year")
    plt.ylabel("Normalized Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig("../results/feature_trends_over_years.png")  # Save the figure
    plt.show()

def averarge_popularity_over_the_years(spotify, yearly_avg):
    plt.figure(figsize=(10,6))

    plt.plot(yearly_avg.index, yearly_avg['popularity'], marker='o')

    plt.title("Average Popularity Over Years")
    plt.xlabel("Year")
    plt.ylabel("Popularity")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../results/average_popularity_over_years.png")  # Save the figure
    plt.show()

def relation_between_each_feature_and_popularity(spotify):
    features = ['energy', 'danceability', 'valence', 'loudness']

    for feature in features:
        plt.figure()
        plt.scatter(spotify[feature], spotify['popularity'])
        plt.xlabel(feature)
        plt.ylabel("popularity")
        plt.title(f"{feature} vs Popularity")
        plt.savefig(f"../results/{feature}_vs_popularity.png")  # Save the figure
        plt.show()

def elbow_method_for_kmeans(inertia, sample_year):
    plt.plot(range(1, 10), inertia, marker='o')
    plt.title(f"Elbow Method ({sample_year})")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.savefig(f"../results/elbow_method_graph_{sample_year}.png")  # Save the figure
    plt.show()

def cluster_graphs_per_year(year_clusters):
    for year in year_clusters:
        data = year_clusters[year]

        cluster_popularity = (
            data.groupby('cluster')['popularity']
            .mean()
        )

        plt.figure()
        cluster_popularity.plot(kind='bar')

        plt.title(f"Cluster vs Popularity ({year})")
        plt.xlabel("Cluster")
        plt.ylabel("Average Popularity")
        plt.savefig(f"../results/cluster_popularity_{year}.png")  # Save the figure
        plt.show()

def pca_scatter_plots(year_clusters):
    for year in year_clusters:
        data = year_clusters[year]

        plt.figure(figsize=(8,6))

        for cluster in sorted(data['cluster'].unique()):
            cluster_data = data[data['cluster'] == cluster]
            plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster}')

        plt.title(f"PCA Clusters - Year {year}")
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.legend()
        plt.savefig(f"../results/pca_clusters_{year}.png")  # Save the figure
        plt.show()

def pca_popularity_map(year_pca_data, year_clusters):
    for year in year_pca_data:
        data = year_clusters[year]
        pca, _ = year_pca_data[year]

        print(f"\nYear: {year}")
        print("Explained Variance:", pca.explained_variance_ratio_)
        print("Components:\n", pca.components_)
        plt.figure(figsize=(8,6))

        scatter = plt.scatter(
            data['PC1'], data['PC2'],
            c=data['popularity'],
            cmap='viridis'
        )

        plt.colorbar(scatter, label='Popularity')
        plt.title(f"PCA Popularity Map - Year {year}")
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.show()

def billboard_distribution(billboard_match_df):
    plt.figure()
    plt.hist(billboard_match_df['best_rank'].dropna(), bins=20)
    plt.xlabel("Best Billboard Rank")
    plt.ylabel("Number of Songs")
    plt.title("Distribution of Billboard Rankings")
    plt.gca().invert_xaxis()
    plt.savefig("../results/billboard_distribution.png")  # Rank 1 on left (better visualization)
    plt.show()

def spotify_songs_in_billboard(spotify_api_df, billboard_match_df):
    
    # Total songs from Spotify
    total_songs = len(spotify_api_df)

    # Songs matched with Billboard
    matched_songs = billboard_match_df['song'].nunique()

    # Not matched
    not_matched = total_songs - matched_songs

    # Plot
    plt.figure()
    plt.bar(['Present in Billboard', 'Not Present'], [matched_songs, not_matched])
    plt.xlabel("Category")
    plt.ylabel("Number of Songs")
    plt.title("Spotify Songs Presence in Billboard Hot 100")
    plt.savefig("../results/spotify_songs_in_billboard.png")  # Save the figure
    plt.show()

def date_vs_chart(billboard_match_df):
    plt.figure()

    plt.scatter(
        billboard_match_df['release_date'],
        billboard_match_df['rank_date']
    )

    plt.xlabel("Release Date")
    plt.ylabel("Billboard Chart Date")
    plt.title("Release Date vs Billboard Chart Date")
    plt.savefig("../results/release_date_vs_chart_date.png")  # Save the figure
    plt.show()

def delay_analysis(billboard_match_df):
    billboard_match_df['delay_days'] = (
    billboard_match_df['rank_date'] - billboard_match_df['release_date']
    ).dt.days

    plt.figure()
    plt.hist(billboard_match_df['delay_days'].dropna(), bins=20)
    plt.xlabel("Days to Reach Billboard")
    plt.ylabel("Number of Songs")
    plt.title("Delay Between Release and Charting")
    plt.show()