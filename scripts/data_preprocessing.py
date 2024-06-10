import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Download stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load the filtered dataset
df = pd.read_csv('data/australia_tweets.csv')

# Define a function to clean the tweets
def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)  # Remove URLs
    tweet = re.sub(r'@[A-Za-z0-9_]+', '', tweet)  # Remove mentions
    tweet = re.sub(r'#', '', tweet)  # Remove hashtags
    tweet = re.sub(r'RT[\s]+', '', tweet)  # Remove RT
    tweet = re.sub(r'\n', '', tweet)  # Remove new lines
    tweet = re.sub(r'[^A-Za-z\s]', '', tweet)  # Remove non-alphabet characters
    tweet = tweet.lower()  # Convert to lowercase
    tweet_tokens = word_tokenize(tweet)  # Tokenize
    filtered_words = [word for word in tweet_tokens if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(filtered_words)

# Clean the tweets
df['Cleaned_Tweet'] = df['text'].apply(clean_tweet)

# Geocoding locations
geolocator = Nominatim(user_agent="geoapiExercises")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def geocode_location(location):
    try:
        location = geolocator.geocode(location)
        return location.latitude, location.longitude
    except:
        return None, None

df['Latitude'], df['Longitude'] = zip(*df['location'].apply(lambda x: geocode_location(x) if pd.notnull(x) else (None, None)))

# Save cleaned data with geocoded locations
df.to_csv('data/cleaned_australia_tweets.csv', index=False)
print("Tweets cleaned, geocoded, and saved to 'data/cleaned_australia_tweets.csv'")
