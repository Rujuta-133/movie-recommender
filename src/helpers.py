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
