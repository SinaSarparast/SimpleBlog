from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.show_article, name='official_translation'),
    path('edith_article',views.edith_article, name='edith_article')
]
