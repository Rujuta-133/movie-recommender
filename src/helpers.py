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