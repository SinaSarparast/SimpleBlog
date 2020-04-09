from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Tag(models.Model):
    name = models.CharField(max_length=25)

class Post(models.Model):
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=400)
    author = User()
    category = models.ForeignKey(
        'Category',
        on_delete   =  models.SET_NULL,
        blank   =   True,
        null    =   True
    )
    rating = models.IntegerField(null=True,blank=True)
    lastmodiefied_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag,null=True,blank=True)
    content = models.TextField()

class Category(models.Model):
    subcategory = models.ForeignKey(
        'Category',
        on_delete   =  models.SET_NULL,
        blank   =   True,
        null    =   True
    )
    name = models.CharField(max_length=255)
