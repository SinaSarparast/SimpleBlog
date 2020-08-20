from django.db import models
from django.contrib.auth.models import User

class Profile(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imge = models.ImageField(defult='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
