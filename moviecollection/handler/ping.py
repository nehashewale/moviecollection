from flask_restful import Resource
from moviecollection.middleware.counter import request_counter

class Ping(Resource):
    @request_counter
    def get(self):
        return {"response" : "All OK"}
    
    
class Index(Resource):
    def get(self):
        return {"response" : "Server is running"}