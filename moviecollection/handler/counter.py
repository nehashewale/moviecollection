
from flask_restful import Resource
from middleware.counter import get_counter, reset_counter

class Counter(Resource):
    def get(self): 
        request_count = get_counter()
        if not request_count:
            request_count = 0
        return { "requests" : request_count}

    def post(self):
        reset_counter()
        return {"message": "request count reset successfully"}