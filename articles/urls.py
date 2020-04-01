from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('official_translation',views.show_article, name='official_translation'),
    path('edith_article',views.edith_article, name='edith_article')
]
