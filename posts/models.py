from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from profiles.models import Profile
import uuid
# Create your models here.

class Post(models.Model):
    user = models.TextField(max_length=300, default="blank")
    body = models.TextField()
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='blank')


    def __str__(self):
        return str(self.body)[:30]

    @property
    def no_of_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    user = models.TextField(max_length=300, default="blank")
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=300, default="blank")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)