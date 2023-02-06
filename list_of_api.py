GET: "https://demo.credy.in/api/v1/maya/movies/"


POST: "http://localhost:8000/register/"
# "Request Payload":

# {
#     "“username”": <desired username>,
#     "“password”": <desired password>
# }

# Response:

# {
#     “access_token”: <Access Token>
# }
 
GET: "http://localhost:8000/movies/"

# {
#     “count”: <total number of movies>,
#     “next”: <link for next page, if present>,
#     “previous”: <link for previous page>,
#     “data”: [
#         {
#             “title”: <title of the movie>,
#             “description”: <a description of the movie>,
#             “genres”: <a comma separated list of genres, if present>,
# 		 “uuid”: <a unique uuid for the movie>
#         },
#         ...
#     ]
# }

GET: "http://localhost:8000/collection/"
# {
#     “is_success”: True,
#     “data”: {
#         “collections”: [
#             {
#                 “title”: “<Title of my collection>”,
#                 “uuid”: “<uuid of the collection name>”
#                 “description”: “My description of the collection.”
#             },
#             ...
#         ],
#         “favourite_genres”: “<My top 3 favorite genres based on the movies I have added in my collections>.”
#     }
# }

POST: "http://localhost:8000/collection/"
# {
#     “title”: “<Title of the collection>”,
#     “description”: “<Description of the collection>”,
#     “movies”: [
#         {
#             “title”: <title of the movie>,
#             “description”: <description of the movie>,
#             “genres”: <generes>,
#             “uuid”: <uuid>
#         }, ...
#     ]
# }

# Response payload:

# {
#     “collection_uuid”: <uuid of the collection item>
# }

PUT: "http://localhost:8000/collection/<collection_uuid>/"

# Request:

# {
#     “title”: <Optional updated title>,
#     “description”: <Optional updated description>,
#     “movies”: <Optional movie list to be updated>,
# }

GET: "http://localhost:8000/collection/<collection_uuid>/"

# Response:

# {
#     “title”: <Title of the collection>,
#     “description”: <Description of the collection>,
#     “movies”: <Details of movies in my collection>
# }



DELETE:" http://localhost:8000/collection/<collection_uuid>/"

GET: "http://localhost:8000/request-count/"

# Response:
# {
#     “requests”: <number of requests served by this server till now>.
# }

POST: "http://localhost:8000/request-count/reset/"

# Response:
# {
#     “message”: “request count reset successfully”
# }





