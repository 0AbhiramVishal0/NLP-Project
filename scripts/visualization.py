import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Load the data
df = pd.read_csv('data/nlp_australia_tweets.csv')

# Create a pseudo-date column (for demonstration purposes)
df['PseudoDate'] = pd.to_datetime(df['DateTime'])

# Time Series Analysis with Matplotlib
tweet_counts = df.set_index('PseudoDate').resample('D').size()
plt.figure(figsize=(10, 5))
plt.plot(tweet_counts.index, tweet_counts.values, label='Tweet Counts')
plt.title('Time Series Analysis of Tweet Volume')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.legend()
plt.savefig('app/static/images/time_series_analysis.png')
plt.show()
plt.close()

# Sentiment Analysis Distribution with Matplotlib
plt.figure(figsize=(10, 5))
df['Sentiment'].value_counts().plot(kind='bar')
plt.title('Sentiment Analysis Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.savefig('app/static/images/sentiment_distribution.png')
plt.show()
plt.close()

# Geographical Distribution with Matplotlib
if 'Longitude' in df.columns and 'Latitude' in df.columns:
    plt.figure(figsize=(10, 5))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    base = world.plot(color='white', edgecolor='black')
    df_geo = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    df_geo.plot(ax=base, marker='o', color='red', markersize=5)
    plt.title('Geographical Distribution of Tweets')
    plt.savefig('app/static/images/geographical_distribution.png')
    plt.show()
    plt.close()
else:
    print("Longitude and Latitude columns are not available in the dataset.")

