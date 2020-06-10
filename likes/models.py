from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from posts.models import Post
# Create your models here.

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)



class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='LIKE', max_length =8)


    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"