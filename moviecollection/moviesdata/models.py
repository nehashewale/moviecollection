from django.db import models
from uuid import uuid4

class User(models.Model):
    username = models.CharField(max_length=255, default=uuid4, db_index=True)
    password = models.CharField(max_length=255)
    accesstoken = models.CharField(max_length=255, default=uuid4)
    created_on = models.DateTimeField(auto_now_add=True)

class Movie(models.Model):
    title = models.CharField(max_length=1023, db_index=True)
    description = models.CharField(max_length=1023)
    genres = models.CharField(max_length=1023)
    uuid = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

class Collection(models.Model):
    uuid = models.CharField(max_length=255)
    title = models.CharField(max_length=1023, db_index=True)
    description = models.CharField(max_length=1023)
    movies = models.ManyToManyField("Movie")
    archive = models.CharField(max_length=1023, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True) 
