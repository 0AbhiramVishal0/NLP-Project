from flask import render_template
from app import app
import pandas as pd
import os

@app.route('/')
def index():
    file_path = os.path.join('data', 'nlp_australia_tweets.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('index.html', tables=[df.to_html(classes='table table-bordered', header="true").strip()], titles=df.columns.values)
    else:
        return render_template('index.html', tables=None, titles=None)

@app.route('/fake_tweets')
def fake_tweets():
    file_path = os.path.join('data', 'fake_tweets.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('fake_tweets.html', tables=[df.to_html(classes='table table-bordered', header="true").strip()], titles=df.columns.values)
    else:
        return "No data available. Please run the fake tweet detection script first."

@app.route('/real_tweets')
def real_tweets():
    file_path = os.path.join('data', 'real_tweets.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('real_tweets.html', tables=[df.to_html(classes='table table-bordered', header="true").strip()], titles=df.columns.values)
    else:
        return "No data available. Please run the fake tweet detection script first."

@app.route('/evaluation')
def evaluation():
    file_path = os.path.join('data', 'evaluation.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('evaluation.html', tables=[df.to_html(classes='table table-bordered', header="true").strip()], titles=df.columns.values)
    else:
        return "No data available. Please run the evaluation script first."

@app.route('/sentiment_map')
def sentiment_map():
    return render_template('sentiment_map.html')

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/top_topics')
def top_topics():
    return render_template('top_topics.html')

@app.route('/misinformation_alerts')
def misinformation_alerts():
    return render_template('misinformation_alerts.html')

@app.route('/entity_extractor')
def entity_extractor():
    return render_template('entity_extractor.html')
