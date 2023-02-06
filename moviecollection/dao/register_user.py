import django;django.setup()
import uuid

from moviecollection.moviesdata.models import User

def get_user_by_username(username):
    try:
        user = User.objects.get(username=username)
        return user
    except Exception as e:
        return None

def create_user(user_name,password):
    user = User.objects.create(
        username = user_name,
        password = password,
        accesstoken= uuid.uuid4().hex
        )
    return user

