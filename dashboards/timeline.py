import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/nlp_australia_tweets.csv')

# Create a pseudo-date column (for demonstration purposes)
df['PseudoDate'] = pd.to_datetime(df['DateTime'])

# Time Series Analysis with Plotly
tweet_counts = df.set_index('PseudoDate').resample('D').size().reset_index(name='Counts')

fig = px.line(tweet_counts, x='PseudoDate', y='Counts', title='Tweet Volume Over Time')
fig.write_html('app/templates/timeline.html')
