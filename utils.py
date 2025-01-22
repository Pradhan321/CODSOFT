import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Function to create a user-item matrix
def create_user_item_matrix(ratings):
    return ratings.pivot(index="UserID", columns="MovieID", values="Rating").fillna(0)

# Function to calculate user-user similarity
def calculate_similarity(user_item_matrix):
    return cosine_similarity(user_item_matrix)

# Function to recommend movies for a specific user
def recommend_movies(user_id, user_item_matrix, similarity_matrix, top_n=5):
    user_index = user_id - 1  # User IDs are 1-indexed
    similar_users = similarity_matrix[user_index]

    # Weighted average of ratings based on similarity
    weighted_ratings = similar_users @ user_item_matrix
    movie_scores = pd.Series(weighted_ratings, index=user_item_matrix.columns)

    # Exclude movies the user has already rated
    rated_movies = user_item_matrix.loc[user_id][user_item_matrix.loc[user_id] > 0].index
    recommendations = movie_scores.drop(rated_movies).sort_values(ascending=False).head(top_n)

    return recommendations
