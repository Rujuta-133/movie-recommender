import pandas as pd

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


def recommend_movies(user_preferences, movies, user_ratings):
    recommendations = {}
    for user_id, genre_prefs in user_preferences.items():
        #top_genre = max(genre_prefs, key = genre_prefs.get)
        sorted_genres = sorted(genre_prefs, key= lambda k: genre_prefs[k], reverse = True)
        for genre in sorted_genres:
            candidate_movies = []
            for movie in movies:
                already_watched = False
                if genre in movie["genres"]:
                    for rating in user_ratings[user_id]:
                        if rating["movie_id"] == movie["movie_id"]:
                            already_watched = True
                            break
                    if already_watched == False:
                        candidate_movies.append(movie)
            if len(candidate_movies) != 0:
                break
        candidate_movies.sort(key = lambda movie: movie["imdb_rating"], reverse=True)
        top_movies = candidate_movies[:3]
        recommendations[user_id] = top_movies
    
    return recommendations


def create_training_dataset(ratings, movies, user_preferences, get_movie_by_id):
    training_data = []
    for rating in ratings:
        user_id = rating["user_id"]
        movie_id = rating["movie_id"]
        movie = get_movie_by_id(movies, movie_id)
        genres = movie["genres"]
        user_genre_score = 0
        for genre in genres:
            user_genre_score += user_preferences[user_id].get(genre, 0)
        if rating["rating_value"] >= 4:
            liked = 1
        else:
            liked = 0
        row = {"user_genre_score" : user_genre_score, "imdb_rating": movie["imdb_rating"], "rating_count": movie["rating_count"], "liked": liked}

        training_data.append(row)
    
    return training_data

def create_user_movie_features(user_id, movie, user_preferences):
    user_genre_score = 0
    genres = movie["genres"]
    for genre in genres:
        user_genre_score += user_preferences[user_id].get(genre, 0)
    imdb_rating = movie["imdb_rating"]
    rating_count = movie["rating_count"]

    feature = {"user_genre_score" : user_genre_score, "imdb_rating": imdb_rating, "rating_count" : rating_count}

    return feature

def recommend_movies_ml(user_id, movies, model, user_preferences, user_ratings):
    results = []
    for movie in movies:
        user_ratings_list = user_ratings[user_id]
        
        already_watched = False
        for rating in user_ratings_list:
            rated_movie_id = rating["movie_id"]
            if rated_movie_id == movie["movie_id"]:
                already_watched = True
                break
        if already_watched:
            continue

        features_dict = create_user_movie_features(user_id, movie, user_preferences)
        features_df = pd.DataFrame([features_dict])
        liked_probability = model.predict_proba(features_df)[0][1]
        
        results.append((movie["movie_id"], liked_probability)) 
    
    results.sort(key = lambda x: x[1], reverse=True)
    top_movies = results[:3]

    recommended_movies = []
    for movie_id,probability in top_movies:
        movie = get_movie_by_id(movies, movie_id)

        if movie:
            title = movie["title"]
            recommended_movies.append((title, probability))
        

    return recommended_movies








