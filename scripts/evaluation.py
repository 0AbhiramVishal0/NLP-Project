import pandas as pd
from sklearn.metrics import classification_report

# Load the datasets
fake_tweets = pd.read_csv('data/fake_tweets.csv')
real_tweets = pd.read_csv('data/real_tweets.csv')

# Create labels
fake_tweets['Label'] = 1
real_tweets['Label'] = 0

# Combine datasets
df = pd.concat([fake_tweets, real_tweets])

# Assuming we have a ground truth column named 'True_Label'
report = classification_report(df['True_Label'], df['Label'], output_dict=True)
report_df = pd.DataFrame(report).transpose()

# Save the evaluation report
report_df.to_csv('data/evaluation_report.csv', index=True)
print("Model evaluation completed and report saved to 'data/evaluation_report.csv'")
