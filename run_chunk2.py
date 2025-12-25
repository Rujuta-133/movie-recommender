from data.sample_data import movies, ratings
from src.helpers import counting_avg, get_movie_by_id



print(counting_avg(movies[0]))

movie1 = get_movie_by_id(movies, 3)
print(movie1["title"])


