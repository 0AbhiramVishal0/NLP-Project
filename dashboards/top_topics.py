import pandas as pd
import plotly.express as px
from gensim import corpora, models

# Load the data
df = pd.read_csv('data/nlp_australia_tweets.csv')

# Topic Modeling using LDA
texts = [tweet.split() for tweet in df['Cleaned_Tweet']]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

topics = lda.show_topics(formatted=False)
data_flat = [item for sublist in texts for item in sublist]
counter = pd.DataFrame(topics, columns=['Topic', 'Words'])

fig = px.bar(counter, x='Topic', y=[len(topic[1]) for topic in topics], title='Top Topics Discussed')
fig.write_html('app/templates/top_topics.html')
