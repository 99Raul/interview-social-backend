from django.db.models.signals import post_save
from django.dispatch import receiver
from likes.models import Like
from .models import Post

@receiver(post_save, sender=Post)
def post_save_like(sender, instance, created, **kwargs):
    obj, created = Like.objects.get_or_create(user=instance.user, post=instance)
    if created:
        obj.value = 'Like'
    else:
        if obj.value=='Like':
            obj.value='Unlike'
        else:
            obj.value='Like'
    obj.save()