Sure, here is the updated `README.md` file with the new section on the dataset:

---

# Social Media Analytics for Emergency Crisis Coordination

## Project Overview

This project leverages social media data to enhance emergency crisis coordination. By analyzing tweets related to natural disasters, we aim to provide valuable insights that can aid emergency teams, government bodies, and media organizations in disaster response and management.

## Project Structure

```plaintext
emergency_crisis_coordination/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── fake_tweets.html
│       ├── real_tweets.html
│       ├── evaluation.html
│       ├── sentiment_map.html
│       ├── heatmap.html
│       ├── timeline.html
│       ├── top_topics.html
│       ├── misinformation_alerts.html
│       └── entity_extractor.html
├── data/
│   ├── australia_shapefile/
│   │   └── Australia.prj
│   │   └── Australia.dbf
│   │   └── Australia.shp
│   │   └── Australia.shx
│   │   └── Australia.xml
│   └── australia_tweets.csv
│   └── cleaned_australia_tweets.csv
│   └── evaluation.csv
│   └── fake_tweets.csv
│   └── real_tweets.csv
│   └── nlp_australia_tweets.csv
│   └── train.csv
├── scripts/
│   ├── load_and_examine.py
│   ├── filter_australia_tweets.py
│   ├── data_preprocessing.py
│   ├── nlp_analysis.py
│   ├── fake_tweet_detection.py
│   ├── geographical_analysis.py
│   └── visualization.py
│   └── evaluation.py
├── dashboards/
│   ├── sentiment_map.py
│   ├── heatmap.py
│   ├── timeline.py
│   ├── top_topics.py
│   ├── misinformation_alerts.py
│   └── entity_extractor.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Dataset

The primary dataset used in this project is obtained from two sources:
the dataset contains the tweets from all over the world, so in preprocessing we filter out all the tweets related to Australia and continue NLP analysis on that cleaned data set.

1. **Kaggle**: The dataset is sourced from the Kaggle competition "Natural Language Processing with Disaster Tweets". The dataset consists of tweets that are labeled as either related to a disaster or not. You can find the dataset [here](https://www.kaggle.com/competitions/nlp-getting-started/data).

2. **Tweepy**: Additional tweets were fetched using the Tweepy library to supplement the Kaggle dataset. Tweepy is a Python library that provides easy access to the Twitter API, allowing us to fetch real-time tweets related to specific keywords and locations.

The combined dataset includes various columns such as:
- `id`: Unique identifier for each tweet.
- `keyword`: Disaster-related keyword from the tweet.
- `location`: Location from where the tweet was sent.
- `text`: The content of the tweet.
- `target`: Label indicating whether the tweet is about a disaster (1) or not (0).
- `Sentiment`: The sentiment of the tweet (Positive, Negative, Neutral).
- `Latitude` and `Longitude`: Geographical coordinates extracted from the location.
- `DateTime`: The date and time when the tweet was posted.

The dataset file used in this project is `train.csv`.
the rest of .csv file are obtained from preprocessing with script files.

## Installation

### Prerequisites

- Python 3.x
- Docker (optional for containerization)
- Hugging Face Transformers
- Windows Subsystem for Linux (WSL) for Docker on Windows

### Clone the Repository

```bash
git clone https://github.com/yourusername/emergency_crisis_coordination.git
cd emergency_crisis_coordination
```

### Create and Activate Virtual Environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Hugging Face Transformers

```bash
pip install transformers
```

### Login to Hugging Face

1. Create an account on [Hugging Face](https://huggingface.co/).
2. Generate an access token from your Hugging Face account settings.
3. Login using the access token:

```bash
huggingface-cli login
```

### Install WSL for Docker on Windows

1. **Install WSL**:
   - Open PowerShell as Administrator and run:
     ```bash
     wsl --install
     ```

2. **Install a Linux distribution** (e.g., Ubuntu) from the Microsoft Store.

3. **Set up WSL**:
   - Open your installed Linux distribution and follow the setup instructions.

4. **Install Docker Desktop**:
   - Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
   - Ensure WSL integration is enabled in Docker Desktop settings.

## Data Preprocessing

### Load and Examine Data

```bash
python scripts/load_and_examine.py
```

### Filter Australia Tweets

```bash
python scripts/filter_australia_tweets.py
```

### Data Preprocessing

```bash
python scripts/data_preprocessing.py
```

## NLP Analysis

### Perform NLP Analysis

```bash
python scripts/nlp_analysis.py
```

### Fake Tweet Detection

```bash
python scripts/fake_tweet_detection.py
```

## Geographical and Temporal Analysis

### Geographical Analysis

```bash
python scripts/geographical_analysis.py
```

### Visualization

```bash
python scripts/visualization.py
```

## Evaluation

### Run Evaluations

```bash
python scripts/evaluation.py
```

## Visualization Dashboards

### Generate Dashboards

```bash
python dashboards/sentiment_map.py
python dashboards/heatmap.py
python dashboards/timeline.py
python dashboards/top_topics.py
python dashboards/misinformation_alerts.py
python dashboards/entity_extractor.py
```

## Run Flask Application

### Set Environment Variable

#### On Windows:

```bash
set FLASK_APP=app
```

#### On macOS/Linux:

```bash
export FLASK_APP=app
```

### Run the Application

```bash
flask run
```

Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Docker

### Build Docker Image

```bash
docker build -t abhiramvishal/emergency_crisis_coordination .
```

### Run Docker Container

```bash
docker run -p 5000:5000 abhiramvishal/emergency_crisis_coordination
```

### Pulling Docker Container
```bash
docker pull abhiramvishal/emergency_crisis_coordination
```

## Project Evaluation

### Sentiment Analysis

Evaluates the sentiment analysis model using metrics like accuracy, precision, recall, and F1-score.

### Fake Tweet Detection

Evaluates the fake tweet detection model using metrics like accuracy, precision, recall, and F1-score.

### Topic Modeling

Evaluates the coherence and perplexity of the topics generated by the model.

### Geographical Analysis

Assesses the coverage of affected areas by comparing with actual disaster reports.

### Temporal Analysis

Correlates tweet volumes with actual event timelines to evaluate temporal accuracy.

## Links

- **Docker Image:** [Docker Hub Link](https://hub.docker.com/repository/docker/abhiramvishal/emergency_crisis_coordination)

---

This `README.md` provides a comprehensive guide to setting up, running, and understanding the project. It includes all the necessary details and steps for installation, data preprocessing, analysis, visualization, and evaluation, along with instructions for setting up and using Docker and Hugging Face.

---