from django.urls import path

from . import views

urlpatterns = [
    path('',    views.index, name='index'),
    path('add/', views.ArticleCreate.as_view(), name='article-add'),
    path('read/<str:slug>',     views.ReadView.as_view(), name='read_article'),
    path('update/<str:slug>',   views.Update.as_view(), name='update_article'),
    path('delete_article/<str:slug>',    views.delete_article, name='delete_article')
]
