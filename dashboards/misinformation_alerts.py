import pandas as pd
import plotly.express as px

# Load the fake and real tweets datasets
df_fake = pd.read_csv('data/fake_tweets.csv')
df_real = pd.read_csv('data/real_tweets.csv')

# Concatenate the datasets
df = pd.concat([df_fake, df_real])

# Check if the Fake_Score column exists
if 'Fake_Score' not in df.columns:
    print("Error: The 'Fake_Score' column is missing from the dataset. Please ensure the fake tweet detection script has been run successfully.")
else:
    # Create a scatter plot for misinformation alerts
    fig = px.scatter(df, x='Longitude', y='Latitude', color='Fake_Score',
                     hover_name='Cleaned_Tweet', title='Misinformation Alerts')
    fig.write_html('app/templates/misinformation_alerts.html')
    print("Misinformation alerts dashboard generated.")

