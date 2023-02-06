
import django;django.setup()
import uuid

from moviecollection.moviesdata.models import Collection, Movie

def get_collection_by_uuid(collection_uuid):
    try:
        collection = Collection.objects.get(uuid=collection_uuid, archive=False)
        return collection
    except:
        return None

def get_collection_by_collection_title(title):
    try:
        collection = Collection.objects.get(title=title, archive=False)
        return collection
    except Exception as e:
        return None

def archive_collection(collection_uuid):
    try:
        collection = Collection.objects.get(uuid=collection_uuid)
        collection.archive = True
        collection.save()
        return True
    except Exception as e:
        return False

def create_collection(title, description):
    collection = Collection.objects.create(
        title = title,
        description = description,
        uuid= uuid.uuid4().hex,
        archive=False
        )
    return collection

def create_movie(title, description, genres, uuid):
    collection = Movie.objects.create(
        title = title,
        description = description,
        genres=genres,
        uuid=uuid,
        )
    return collection