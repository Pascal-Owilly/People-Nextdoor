from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



# Extending User Model Using a One-To-One Link

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='your username')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()
    general_location = models.TextField()
    about_me = models.TextField()
    neighbourhood_name = models.TextField()
  



    def __str__(self):
        return f'{self.user.username} Profile'
