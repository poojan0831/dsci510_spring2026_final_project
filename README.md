# The Evolution of Popular Music Over Two Decades: Patterns and Popularity
This project analyzes the evolution of popular music from 2000 to 2020 by examining how musical characteristics such as Energy, Mood and Style have changed over time. Using a dataset of top Spotify tracks, the study explores how features like Danceability, Loudness, Tempo and Valence influence song popularity and how these relationships vary across different years. Through detailed Exploratory Data Analysis and Visualization, the project identifies key patterns in listener preferences and highlights shifts in musical trends over two decades.

To further understand these patterns, the project applies Machine Learning techniques such as K-Means clustering to group songs into meaningful categories, including iHgh-Energy, Balanced, and Low-Energy/Emotional tracks. Dimensionality reduction using Principal Component Analysis (PCA) is also performed to interpret underlying structures in the data, helping to explain how different musical attributes combine to define song characteristics.

In addition, the project integrates external data sources, including the Spotify API and Billboard Hot 100 dataset, to enrich the analysis. By comparing song release metadata with chart performance, the project investigates how quickly songs gain popularity and whether they chart immediately after release. Overall, this project provides a data-driven perspective on how popular music has evolved and what factors contribute to a song’s success over time.

# Data sources
## Data Sources

| Data source # | Name / short description | Source URL | Type (API / File) | List of fields | Format | Accessed with Python? | Estimated size |
|--------------|------------------------|------------|-------------------|----------------|--------|------------------------|----------------|
| 1 | Top Hits Spotify (2000–2019) [Primary Dataset] | https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019/data | File | artist, song, duration, popularity, year, danceability, energy, loudness, tempo, genre, liveliness, valence | CSV | Yes | ~2000 |
| 2 | Spotify API [For Extra Insights to Original Data] | https://developer.spotify.com/documentation/web-api | API | song name, artist, release date, album name | JSON | Yes | ~1000 |
| 3 | Billboard Hot 100 Songs | https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs | File | date, rank, artist, song | CSV | Yes | ~1000 |

# Results 
## Key Analysis

### 1. Feature–Popularity Relationship
Correlation analysis showed that no individual audio feature strongly correlates with popularity. Features like energy and loudness are related to each other, but not directly to popularity. This indicates that song success depends on a combination of attributes rather than a single factor.

---

### 2. Evolution of Music Trends
Year-wise analysis revealed that:
- Early 2000s songs were dominated by high energy and loudness.
- Over time, music became more balanced.
- Danceability and emotional tone (valence) gained importance in later years.

This suggests a shift toward more diverse and expressive music styles.

---

### 3. Clustering (K-Means)
Songs were grouped into three clusters based on audio features:
- **High Energy Songs:** Loud and energetic tracks.
- **Balanced Songs:** Moderate across all features.
- **Low Energy / Emotional Songs:** Calm or expressive tracks.

Clustering showed that combinations of features define song types more effectively than individual features.

---

### 4. PCA (Dimensionality Reduction)
Principal Component Analysis reduced the feature space into:
- **Intensity (PC1):** Driven by energy and loudness.
- **Emotion/Rhythm (PC2):** Influenced by valence and danceability.

This helped visualize the structure of music and confirmed the separation between different song types.

---

### 5. Spotify API Enrichment
Spotify API was used to retrieve metadata (album and release date) for top songs across different time periods. This enabled temporal analysis and integration with Billboard data.

---

### 6. Billboard Comparison
Spotify songs were matched with Billboard rankings using song name, artist, and a 90-day window after release.

Key findings:
- Not all popular Spotify songs appear on Billboard charts.
- Chart success is more selective and influenced by external factors.
- Most songs take time after release to achieve chart success.
- Only a small number of songs reach top rankings.


# Installation
This project uses the Spotify API for accessing song metadata. You can obtain a free API token from the Spotify Developer Dashboard by logging into the Spotify Developers website.

After generating the token, create a `.env` file in the root directory of the project and store your token as follows:

`SPOTIFY_API_TOKEN=your_token_here`

The project relies only on standard Python data science libraries, including `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `python-dotenv` and `requests`.

To install all required dependencies, run:
 `pip install -r requirements.txt`

# Running analysis 

Download the Top Hits Spotify (2000–2019) and Billboard Hot 100 Songs datasets from the links provided in the Data Sources table, and place them in the `data/` directory.

Complete the setup by following the steps in the Installation section (including configuring the `.env` file and installing dependencies).

Navigate to the `src/` directory and run the main script:

`python main.py `

After execution, all generated visualizations and outputs will be saved in the `results/` directory.
