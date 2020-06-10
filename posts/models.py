from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# from profiles.models import Profile
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return str(self.body)[:30]

    @property
    def no_of_likes(self):
        return self.liked.all().count()

    class Meta:
        ordering = ('-created',)
