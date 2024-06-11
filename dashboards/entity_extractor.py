import pandas as pd
import plotly.express as px
import spacy

# Load the data
df = pd.read_csv('data/nlp_australia_tweets.csv')

# Load Spacy model
nlp = spacy.load('en_core_web_sm')

# Extract entities
def get_entities(text):
    doc = nlp(text)
    return [(entity.text, entity.label_) for entity in doc.ents]

df['Entities'] = df['Cleaned_Tweet'].apply(get_entities)

# Flatten entity data for visualization
entities = df['Entities'].explode().dropna().tolist()
entity_df = pd.DataFrame(entities, columns=['Entity', 'Label'])

fig = px.treemap(entity_df, path=['Label', 'Entity'], title='Extracted Entities')
fig.write_html('app/templates/entity_extractor.html')
