# app/recommendation.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_videos(user_videos, all_videos, top_n=3):
    """
    user_videos: list of strings (titles of videos the user has watched)
    all_videos: list of strings (all available video titles)
    """
    if not user_videos:
        return all_videos[:top_n]  # fallback

    # Combine user videos + all videos
    corpus = user_videos + all_videos
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Compute cosine similarity between user videos and all videos
    user_matrix = tfidf_matrix[:len(user_videos)]
    all_matrix = tfidf_matrix[len(user_videos):]

    similarity = cosine_similarity(user_matrix, all_matrix)
    # Take average similarity across user's watched videos
    avg_similarity = similarity.mean(axis=0)

    # Get top N recommended indices
    top_indices = avg_similarity.argsort()[::-1][:top_n]
    recommended = [all_videos[i] for i in top_indices]
    return recommended
