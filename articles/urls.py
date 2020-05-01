from django.urls import path

from . import views

urlpatterns = [
    path('',    views.index, name='index'),
    path('create_article/',    views.create_article, name='create_article'),
    path('read_article/<str:slug>',     views.read_article, name='read_article'),
    path('update_article/<str:slug>',    views.update_article, name='update_article'),
    path('delete_article/<str:slug>',    views.delete_article, name='delete_article')

]
