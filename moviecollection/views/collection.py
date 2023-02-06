
def get_response(collection):
    movie_list = []
    for movie in collection.movies.all():
        movie_list.append({
            "title": movie.title,
            "description" : movie.description,
            "genres": movie.genres,
            "uuid" : movie.uuid
        })

    response = {
        "title": collection.title,
        "description" : collection.description,
        "movies": movie_list
        }
    return response