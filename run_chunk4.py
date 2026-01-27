from data.sample_data import movies, ratings
from src.helpers import user_ratings_map, user_genre_preferences, get_movie_by_id

# Step 1: Build user -> ratings mapping (Chunk 3 output)
user_ratings = user_ratings_map(ratings)

# Step 2: Compute user -> genre preferences (Chunk 4)
user_preferences = user_genre_preferences(
    user_ratings=user_ratings,
    movies=movies,
    get_movie_by_id=get_movie_by_id
)

# Step 3: Basic sanity checks
print("Type of output:", type(user_preferences))
print("Number of users:", len(user_preferences))

# Step 4: Inspect one user in detail
print("\nGenre preferences for user_1:")
print(user_preferences.get("user_1"))

# Step 5: Inspect all users (optional, but useful)
print("\nAll user genre preferences:")
for user_id, prefs in user_preferences.items():
    print(user_id, "->", prefs)
