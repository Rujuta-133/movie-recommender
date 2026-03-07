import pandas as pd

from data.sample_data import movies, ratings

from src.helpers import (
    user_ratings_map,
    user_genre_preferences,
    create_training_dataset,
    recommend_movies_ml,
    get_movie_by_id
)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Step 1 — Build user structures
user_ratings = user_ratings_map(ratings)

user_preferences = user_genre_preferences(
    user_ratings,
    movies,
    get_movie_by_id
)


# Step 2 — Build training dataset
training_data = create_training_dataset(
    ratings,
    movies,
    user_preferences,
    get_movie_by_id
)

df = pd.DataFrame(training_data)


# Step 3 — Prepare features and labels
X = df[["user_genre_score", "imdb_rating", "rating_count"]]
y = df["liked"]


# Step 4 — Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)


# Step 5 — Choose a user
user_id = "user_1"


# Step 6 — Get recommendations
recommendations = recommend_movies_ml(
    user_id,
    movies,
    model,
    user_preferences,
    user_ratings
)


# Step 7 — Print results
print("\nRecommended movies:\n")

for title, probability in recommendations:
    print(f"{title} — {round(probability, 2)}")