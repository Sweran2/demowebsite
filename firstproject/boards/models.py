from django.db import models
from django.contrib.auth.models import User
# this will summon user table

# One great thing about django you can deal with any typof database

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    # relation Topic table with User table foregin key
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    # relation Topic table with Board table foregin key

    created_dt = models.DateTimeField(auto_now_add=True)
#   take the date of today and add it

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
