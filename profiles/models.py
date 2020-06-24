from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=200, blank=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='friends')


    def __str__(self):
        return f"{self.user}-{self.created.strftime('%d-%m-%y')}"

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def get_post_no(self):
        return self.posts.all().count()

    def get_like_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value == 'Like':
                total_liked += 1
        return total_liked

    def get_likes_recieved_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.likes.all().count()
        return total_liked

    def __str__(self):
        return self.first_name
    
    def __str__(self):
        return self.last_name


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"