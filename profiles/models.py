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
