import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/nlp_tweets.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Emergency Crisis Coordination Analytics'),

    dcc.Tabs([
        dcc.Tab(label='Time Series Analysis', children=[
            dcc.Graph(id='time-series-chart')
        ]),

        dcc.Tab(label='Sentiment Analysis', children=[
            dcc.Graph(id='sentiment-analysis-chart')
        ]),

        dcc.Tab(label='Geographical Distribution', children=[
            dcc.Graph(id='geo-distribution-chart')
        ]),
    ])
])

@app.callback(
    Output('time-series-chart', 'figure'),
    Input('time-series-chart', 'id')
)
def update_time_series_chart(_):
    tweet_counts = df.set_index('Date').resample('D').size().reset_index(name='Counts')
    fig = px.line(tweet_counts, x='Date', y='Counts', title='Time Series Analysis of Tweet Volume')
    return fig

@app.callback(
    Output('sentiment-analysis-chart', 'figure'),
    Input('sentiment-analysis-chart', 'id')
)
def update_sentiment_analysis_chart(_):
    fig = px.histogram(df, x='Sentiment', nbins=50, title='Sentiment Analysis Distribution')
    return fig

@app.callback(
    Output('geo-distribution-chart', 'figure'),
    Input('geo-distribution-chart', 'id')
)
def update_geo_distribution_chart(_):
    fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', color='Sentiment',
                         hover_name='Tweet', title='Geographical Distribution of Tweets')
    fig.update_geos(projection_type="natural earth")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
