from django.db import models

from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()
    general_location = models.TextField()
    about_me = models.TextField()
    neighbourhood_name = models.TextField()


    def __str__(self):
        return self.user.username
