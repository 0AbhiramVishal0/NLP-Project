import pandas as pd

# Load the dataset
file_path = 'data/train.csv'
df = pd.read_csv(file_path)

# Filter for tweets related to Australia using the 'location' column
australia_tweets = df[df['location'].str.contains('Australia', na=False, case=False)]

# Save the filtered data
australia_tweets.to_csv('data/australia_tweets.csv', index=False)
print("Filtered tweets for Australia and saved to 'data/australia_tweets.csv'")
