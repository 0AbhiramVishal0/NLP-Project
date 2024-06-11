from flask import render_template, send_from_directory
from app import app
import pandas as pd
import os

@app.route('/')
def index():
    file_path = os.path.join('data', 'nlp_australia_tweets.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('index.html', tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)
    else:
        return "No data available. Please run the data processing scripts first."

@app.route('/fake_tweets')
def fake_tweets():
    file_path = os.path.join('data', 'fake_tweets.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('fake_tweets.html', tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)
    else:
        return "No fake tweets detected."

@app.route('/real_tweets')
def real_tweets():
    file_path = os.path.join('data', 'real_tweets.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('real_tweets.html', tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)
    else:
        return "No real tweets detected."

@app.route('/evaluation')
def evaluation():
    file_path = os.path.join('data', 'evaluation_report.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return render_template('evaluation.html', tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)
    else:
        return "No evaluation report available."

@app.route('/static/images/<path:filename>')
def custom_static(filename):
    return send_from_directory('static/images', filename)
