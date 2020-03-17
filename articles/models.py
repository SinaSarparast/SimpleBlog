from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=25)

class Post(models.Model):
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=400)
    author = User()
    rating = models.IntegerField()
    lastmodiefied_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
