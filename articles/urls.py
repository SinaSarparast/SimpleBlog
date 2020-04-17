from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_article/<str:slug>/', views.show_article, name='show_article'),
    path('edith_article',views.edith_article, name='edith_article'),
    path('show_nav',views.show_nav, name='show_nav')
]
