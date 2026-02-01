from data.sample_data import movies, ratings
from src.helpers import (
    user_ratings_map,
    user_genre_preferences,
    recommend_movies,
    get_movie_by_id
)

# Build Chunk 3 output
user_ratings = user_ratings_map(ratings)

# Build Chunk 4 output
user_preferences = user_genre_preferences(
    user_ratings=user_ratings,
    movies=movies,
    get_movie_by_id=get_movie_by_id
)

# Chunk 5: recommendations
recommendations = recommend_movies(
    user_preferences=user_preferences,
    movies=movies,
    user_ratings=user_ratings
)

# Inspect output
print("Type of output:", type(recommendations))
print("\nRecommendations for user_1:")
for movie in recommendations["user_1"]:
    print(movie["title"], "-", movie["imdb_rating"])

print("\nAll recommendations:")
for user_id, recs in recommendations.items():
    print(user_id, "->", [m["title"] for m in recs])
