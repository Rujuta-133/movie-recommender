from data.sample_data import movies, ratings
from src.helpers import (
    get_movie_by_id,
    user_ratings_map,
    user_genre_preferences,
    create_training_dataset
)

# Step 1: build user → ratings mapping
user_ratings = user_ratings_map(ratings)

# Step 2: compute user genre preferences
user_preferences = user_genre_preferences(user_ratings, movies, get_movie_by_id)

# Step 3: build training dataset
training_data = create_training_dataset(ratings, movies, user_preferences, get_movie_by_id)

# Step 4: verify
print("Total rows:", len(training_data))
print("\nFirst row:")
print(training_data[0])
