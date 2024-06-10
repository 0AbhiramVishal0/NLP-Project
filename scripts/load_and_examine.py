import pandas as pd

# Load the dataset
file_path = 'data/train.csv'
df = pd.read_csv(file_path)

# Display basic information about the dataset
print(df.info())
print(df.head())
