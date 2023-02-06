from flask_restful import Resource
from validator.register_user import  validate_user_schema
from flask import request
from dao.register_user import get_user_by_username, create_user
from views.register_user import register_user_response

class RegisterUser(Resource):
    def post(self):
        # getting body 
        body = request.json

        # validate schema 
        # is_valid_schema = validate_user_schema(body)

        # if is_valid_schema == False:
        #     return {"response" : "Invalid Schema"}
        
        user = get_user_by_username(body["username"])
        if user != None:
            reponse = register_user_response(user.accesstoken)
            return reponse
        
        user = create_user(body["username"], body["password"])
        reponse = register_user_response(user.accesstoken)
        return reponse
    
    