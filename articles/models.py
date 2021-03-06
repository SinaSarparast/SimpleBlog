from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=25,blank = True,null = True)
    def __str__(self):
       return self.name


class ArticleAuthor(models.Model):
    """docstring for ArticleAuthor."""

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username


class Post(models.Model):
    # Not possible to use the SlugField. It does not accept unicode characters in
    # django admin page so I had to change it to CharField
    # slug = models.SlugField(_('slug'), max_length=255, unique=True)

    slug    =   models.CharField(max_length=500,unique=True,primary_key=True)
    title   =   models.CharField(max_length=500)
    author  =   models.ForeignKey(
        User,
        on_delete   =   models.SET_NULL,
        null    =   True
        )
    # category    =   models.ForeignKey(
    #     'Category',
    #     on_delete   =  models.SET_NULL,
    #     blank   =   True,
    #     null    =   True
    #     )
    lastmodiefied_date = models.DateField(auto_now=True)
    # tag = models.ForeignKey(
    #     'Tag',
    #     on_delete   =  models.SET_NULL,
    #     blank   =   True,
    #     null    =   True
    # )
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('read_article',kwargs={'slug': self.pk})

    def __str__(self):
       return self.title


class Category(models.Model):
    # post = models.ForeignKey(
    #     'Post',
    #     on_delete   =  models.SET_NULL,
    #     blank   =   True,
    #     null    =   True
    # )
    name = models.CharField(max_length=255)
    def __str__(self):
       return self.name
