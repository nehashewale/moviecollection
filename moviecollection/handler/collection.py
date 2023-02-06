from flask_restful import Resource
from flask import request
from views.collection import get_response
from dao.collection import create_collection, create_movie,get_collection_by_collection_title,archive_collection, get_collection_by_uuid
from moviecollection.middleware.counter import request_counter

class Collection(Resource):
    @request_counter
    def post(self):
        # getting body 
        body = request.json

        collection = get_collection_by_collection_title(body["title"])
        if collection:
            return { "is_success": False}
        collection = create_collection(body["title"], body["description"])
        for movie_data in body["movies"]:
            movie = create_movie(
                movie_data["title"], 
                movie_data["description"], 
                movie_data["genres"], 
                movie_data["uuid"])
            collection.movies.add(movie)

        return { "collection_uuid" : collection.uuid}
    
    # @request_counter
    def put(self, collection_uuid=""):
        # getting body 
        body = request.json

        collection = get_collection_by_uuid(collection_uuid)
        if not collection:
            return { "is_success": False}
        collection.title = body["title"], 
        collection.description = body["description"]
        collection.movies.clear()
        for movie_data in body["movies"]:
            movie = create_movie(
                movie_data["title"], 
                movie_data["description"], 
                movie_data["genres"], 
                movie_data["uuid"])
            collection.movies.add(movie)
        collection.save()

        return { "title" : collection.title}
    
    # @request_counter
    def get(self, collection_uuid=""):      
        collection = get_collection_by_uuid(collection_uuid)
        if not collection:
            return {}
        response = get_response(collection)
        return response
    
    # @request_counter
    def delete(self, collection_uuid=""):
        is_archived = archive_collection(collection_uuid)
        return { "is_success" : is_archived}