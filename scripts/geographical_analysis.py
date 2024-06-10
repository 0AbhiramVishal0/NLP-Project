import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/cleaned_australia_tweets.csv')

# Load a shapefile of Australia for geographical plotting
# You need a shapefile for Australia (e.g., "Australia.shp")
australia = gpd.read_file('data/australia_shapefile/Australia.shp')

# Create a GeoDataFrame with tweet locations
# Ensure that the Latitude and Longitude columns are present
if 'Longitude' in df.columns and 'Latitude' in df.columns:
    df = df.dropna(subset=['Longitude', 'Latitude'])  # Drop rows with missing coordinates
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']))

    # Plot the tweets on the map
    fig, ax = plt.subplots(figsize=(10, 10))
    australia.plot(ax=ax, color='white', edgecolor='black')
    gdf.plot(ax=ax, color='red', markersize=5)
    plt.title('Geographical Distribution of Tweets Related to Disasters in Australia')
    plt.show()
else:
    print("Longitude and Latitude columns are not available in the dataset.")
