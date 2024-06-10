import pandas as pd
from textblob import TextBlob
from gensim import corpora, models
import spacy

def sentiment_analysis(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def topic_modeling(texts, num_topics=5, passes=15):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)
    return lda

def named_entity_recognition(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities
