from django.urls import path
from .views import UpdateProfile

urlpatterns = [
    path('update/<pk>', UpdateProfile.as_view(), name='update_profile')
]
