import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/nlp_australia_tweets.csv')

# Create a density heatmap
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Sentiment_Score',
                        radius=10, center=dict(lat=-25, lon=133), zoom=3,
                        mapbox_style="stamen-terrain", title='Heatmap of Sentiments')
fig.write_html('app/templates/heatmap.html')
