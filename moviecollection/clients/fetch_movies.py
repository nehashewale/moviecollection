
import requests
import json
import logging

def get_movie_collection(page_number):
    response = requests.get(url="https://demo.credy.in/api/v1/maya/movies/?page=" + str(page_number))
    if response.status_code != 200:
        logging.error("External api called failed")
        return None
    response_json = json.loads(response._content)
    return response_json


if __name__=="__main__":
    resp = get_movie_collection(1)
    print(resp)
    