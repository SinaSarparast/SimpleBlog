from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddView.as_view(), name='article-add'),
    path('read/<str:slug>', views.ReadView.as_view(),   name='read_article'),
    path('update/<str:slug>',   views.UpdateView.as_view(), name='update_article'),
    path('delete/<str:slug>',   views.DeleteView.as_view(), name='delete_article')
]
