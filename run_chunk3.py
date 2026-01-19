from data.sample_data import ratings
from src.helpers import user_ratings_map

user_ratings = user_ratings_map(ratings)

print("Type of output:", type(user_ratings))
print("Number of users:", len(user_ratings))

print("\nRatings for user_1:")
print(user_ratings.get("user_1"))

if "user_1" in user_ratings:
    print("Number of ratings by user_1:", len(user_ratings["user_1"]))

print(user_ratings)
          
