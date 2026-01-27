def counting_avg(movie):
    if movie["rating_count"] == 0.0:
        return 0.0
    else:
        return movie["rating_sum"] / movie["rating_count"]
    

def get_movie_by_id(movies, movie_id):
    for movie in movies:
        if movie["movie_id"] == movie_id:
            return movie
    return None

def user_ratings_map(ratings):
    user_ratings = {}
    for rating in ratings:
        user_id = rating["user_id"]
        if user_id not in user_ratings.keys():
           user_ratings[user_id] = []
           
        user_ratings[user_id].append(rating)
            
    return user_ratings

def user_genre_preferences(user_ratings, movies, get_movie_by_id):
    user_preferences = {}
    for user_id, ratings_list in user_ratings.items():
        genre_scores = {}
        for rating in ratings_list:
            movie_id = rating["movie_id"]
            rating_value = rating["rating_value"]
            movie = get_movie_by_id(movies, movie_id)
            genres = movie["genres"]
            for genre in genres:
                if genre in genre_scores.keys():
                    genre_scores[genre] += rating_value
                else:
                    genre_scores[genre] = rating_value
        user_preferences[user_id] = genre_scores

    return user_preferences

