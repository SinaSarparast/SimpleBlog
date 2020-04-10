from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Tag(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
       return self.name

class Post(models.Model):

    # Not possible to use the SlugField. It does not accept unicode characters in
    # django admin page so I had to change it to CharField
    # slug = models.SlugField(_('slug'), max_length=255, unique=True)
    
    slug = models.CharField(max_length=255,unique=True)
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
    tags = models.ForeignKey(
        'Tag',
        on_delete   =  models.SET_NULL,
        blank   =   True,
        null    =   True
    )
    content = models.TextField()
    def __str__(self):
       return self.title

class Category(models.Model):
    subcategory = models.ForeignKey(
        'Category',
        on_delete   =  models.SET_NULL,
        blank   =   True,
        null    =   True
    )
    name = models.CharField(max_length=255)
    def __str__(self):
       return self.name
