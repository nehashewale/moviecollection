from flask import Flask
from flask_restful import Resource, Api
from handler.ping import Ping,Index
from handler.register_user import RegisterUser
from handler.movies import Movie
from handler.collection import Collection
from handler.counter import Counter

app = Flask(__name__)
api = Api(app)
api.add_resource(Index, '/')
api.add_resource(Ping, '/ping/')
api.add_resource(RegisterUser, '/register/')
api.add_resource(Movie, '/movies/')
api.add_resource(Collection, '/collection/<string:collection_uuid>/', '/collection/')
api.add_resource(Counter, '/request-count/', '/request-count/reset/')

if __name__ == '__main__':
    app.run(debug=True, port=8000)