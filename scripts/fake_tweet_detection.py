import pandas as pd
from transformers import pipeline

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_australia_tweets.csv')

# Fake Tweet Detection using a pre-trained model
fake_tweet_detector = pipeline('text-classification', model='roberta-base-openai-detector')

def is_fake_tweet(text):
    result = fake_tweet_detector(text)[0]
    label = result['label']
    score = result['score']
    return label == 'FAKE', score

df[['Is_Fake', 'Fake_Score']] = df['Cleaned_Tweet'].apply(lambda x: pd.Series(is_fake_tweet(x)))

# Separate fake and real tweets
fake_tweets = df[df['Is_Fake']]
real_tweets = df[~df['Is_Fake']]

# Save results
fake_tweets.to_csv('data/fake_tweets.csv', index=False)
real_tweets.to_csv('data/real_tweets.csv', index=False)
print("Fake tweet detection completed and results saved.")
