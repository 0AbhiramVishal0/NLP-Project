from flask import render_template
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
