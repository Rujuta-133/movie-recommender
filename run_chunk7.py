import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from data.sample_data import movies,ratings
from src.helpers import (
    get_movie_by_id,
    user_genre_preferences,
    user_ratings_map,
    create_training_dataset
)

user_ratings = user_ratings_map(ratings)

user_preferences = user_genre_preferences(user_ratings, movies, get_movie_by_id)

training_data =  create_training_dataset(ratings, movies, user_preferences, get_movie_by_id)

df =pd.DataFrame(training_data)

print("Shape:", df.shape)
print("\nColumns: ",df.columns.tolist())
print("\nFirst Rows:")
print(df.head())

X = df.drop(columns=["liked"])
y = df["liked"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Train size:", X_train.shape)
print("Test size:", X_test.shape)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(accuracy)