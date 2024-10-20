# job_recommender.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

def vectorize_and_fit(df, text_column):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df[text_column])
    return X, vectorizer

def recommend_jobs(X, user_input_vector, n_neighbors=5):
    nn = NearestNeighbors(n_neighbors=n_neighbors)
    nn.fit(X)
    distances, indices = nn.kneighbors(user_input_vector)
    return indices
