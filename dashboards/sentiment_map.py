import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/nlp_australia_tweets.csv')

# Geographical Distribution with Plotly
fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', color='Sentiment',
                     hover_name='Cleaned_Tweet', title='Geographical Distribution of Sentiments')
fig.update_geos(projection_type="natural earth")
fig.write_html('app/templates/sentiment_map.html')
