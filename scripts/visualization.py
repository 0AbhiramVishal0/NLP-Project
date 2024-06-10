import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/nlp_australia_tweets.csv')

# Create a pseudo-date column (for demonstration purposes)
df['PseudoDate'] = pd.to_datetime(df['id'], unit='s')

# Time Series Analysis with Plotly
tweet_counts = df.set_index('PseudoDate').resample('D').size().reset_index(name='Counts')

fig = px.line(tweet_counts, x='PseudoDate', y='Counts', title='Time Series Analysis of Tweet Volume')
fig.show()

# Sentiment Analysis Distribution
fig = px.histogram(df, x='Sentiment', nbins=50, title='Sentiment Analysis Distribution')
fig.show()

# Geographical Distribution with Plotly (if longitude and latitude are available)
if 'Longitude' in df.columns and 'Latitude' in df.columns:
    fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', color='Sentiment',
                         hover_name='Cleaned_Tweet', title='Geographical Distribution of Tweets')
    fig.update_geos(projection_type="natural earth")
    fig.show()
else:
    print("Longitude and Latitude columns are not available in the dataset.")
