import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from gensim import corpora, models
from gensim.models.coherencemodel import CoherenceModel
from transformers import pipeline

# Load datasets
df = pd.read_csv('data/nlp_australia_tweets.csv')


# Sentiment Analysis Evaluation
def evaluate_sentiment_analysis(df):
    classifier = pipeline('sentiment-analysis')
    df['Predicted_Sentiment'] = df['Cleaned_Tweet'].apply(lambda x: classifier(x)[0]['label'])
    accuracy = accuracy_score(df['Sentiment'], df['Predicted_Sentiment'])
    precision = precision_score(df['Sentiment'], df['Predicted_Sentiment'], average='weighted')
    recall = recall_score(df['Sentiment'], df['Predicted_Sentiment'], average='weighted')
    f1 = f1_score(df['Sentiment'], df['Predicted_Sentiment'], average='weighted')
    return accuracy, precision, recall, f1

# Topic Modeling Evaluation
def evaluate_topic_modeling(df):
    texts = [tweet.split() for tweet in df['Cleaned_Tweet']]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    coherence_model_lda = CoherenceModel(model=lda, texts=texts, dictionary=dictionary, coherence='c_v')
    coherence_score = coherence_model_lda.get_coherence()
    return coherence_score

# Geographical Analysis Evaluation (Coverage)
def evaluate_geographical_analysis(df):
    covered_areas = df[['Latitude', 'Longitude']].dropna().nunique()
    total_areas = df.shape[0]
    coverage = covered_areas / total_areas
    return coverage

# Temporal Analysis Evaluation (Correlation with Events)
def evaluate_temporal_analysis(df):
    df['PseudoDate'] = pd.to_datetime(df['DateTime'])
    tweet_counts = df.set_index('PseudoDate').resample('D').size()
    actual_event_dates = pd.to_datetime(['2022-01-01', '2022-06-01', '2022-12-01'])
    event_counts = tweet_counts[tweet_counts.index.isin(actual_event_dates)].sum()
    correlation = event_counts / len(actual_event_dates)
    return correlation

if __name__ == '__main__':
    # Perform evaluations
    sentiment_accuracy, sentiment_precision, sentiment_recall, sentiment_f1 = evaluate_sentiment_analysis(df)
    topic_coherence = evaluate_topic_modeling(df)
    geo_coverage = evaluate_geographical_analysis(df)
    temporal_correlation = evaluate_temporal_analysis(df)

    # Save evaluation results
    evaluation_results = {
        'Sentiment Analysis': {
            'Accuracy': sentiment_accuracy,
            'Precision': sentiment_precision,
            'Recall': sentiment_recall,
            'F1 Score': sentiment_f1
        },
        'Topic Modeling': {
            'Coherence Score': topic_coherence
        },
        'Geographical Analysis': {
            'Coverage': geo_coverage
        },
        'Temporal Analysis': {
            'Correlation with Events': temporal_correlation
        }
    }
    df_evaluation = pd.DataFrame.from_dict(evaluation_results, orient='index')
    df_evaluation.to_csv('data/evaluation.csv')

    # Print results
    print("Evaluation completed and results saved to 'data/evaluation.csv'")
