from flask_restful import Resource
from flask import request
from clients.fetch_movies import get_movie_collection
from moviecollection.middleware.counter import request_counter

class Movie(Resource):
    @request_counter
    def get(self):
        # getting params
        params = request.args.to_dict()
        page_number = int(params.get('page_number',1))        
        response = get_movie_collection(page_number)
        return response
    
    