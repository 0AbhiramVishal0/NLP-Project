import pandas as pd
from transformers import pipeline

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_australia_tweets.csv')

# Define emergency-related keywords
emergency_keywords = ['flood', 'fire', 'cyclone', 'earthquake', 'storm']

# Use a pre-trained transformer model for text classification
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

# Define candidate labels for classification
candidate_labels = ['emergency', 'not emergency']

def is_emergency_tweet(text):
    result = classifier(text, candidate_labels)
    scores = result['scores']
    labels = result['labels']
    if labels[0] == 'emergency':
        return False, scores[0]  # Not fake
    else:
        return True, scores[1]  # Fake

df[['Is_Fake', 'Fake_Score']] = df['Cleaned_Tweet'].apply(lambda x: pd.Series(is_emergency_tweet(x)))

# Separate fake and real tweets
fake_tweets = df[df['Is_Fake']]
real_tweets = df[~df['Is_Fake']]

# Save results
fake_tweets.to_csv('data/fake_tweets.csv', index=False)
real_tweets.to_csv('data/real_tweets.csv', index=False)
print("Fake tweet detection completed and results saved.")
