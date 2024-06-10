import pandas as pd
from textblob import TextBlob
from gensim import corpora, models
import spacy

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_australia_tweets.csv')

# Sentiment Analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

df['Sentiment'] = df['Cleaned_Tweet'].apply(get_sentiment)

# Topic Modeling using LDA
texts = [tweet.split() for tweet in df['Cleaned_Tweet']]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

df['Topic'] = [lda[corpus[i]] for i in range(len(corpus))]

# Named Entity Recognition (NER)
nlp = spacy.load('en_core_web_sm')
def get_entities(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

df['Entities'] = df['Cleaned_Tweet'].apply(get_entities)

# Save NLP analysis results
df.to_csv('data/nlp_australia_tweets.csv', index=False)
print("NLP analysis completed and saved to 'data/nlp_australia_tweets.csv'")