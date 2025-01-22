import pandas as pd
from utils import create_user_item_matrix, calculate_similarity, recommend_movies

# Load the dataset
ratings = pd.read_csv('./dataset/ratings.csv')

# Create user-item matrix
user_item_matrix = create_user_item_matrix(ratings)

# Calculate user similarity
similarity_matrix = calculate_similarity(user_item_matrix)

# Recommend movies for a specific user
user_id = 3  # Change this to recommend for other users
recommendations = recommend_movies(user_id, user_item_matrix, similarity_matrix)

# Display recommendations
print(f"Recommendations for User {user_id}:")
for movie_id, score in recommendations.items():
    print(f"Movie ID: {movie_id}, Score: {score:.2f}")
