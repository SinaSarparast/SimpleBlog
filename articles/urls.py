from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('official_translation',views.official_translation, name='official_translation')

]
