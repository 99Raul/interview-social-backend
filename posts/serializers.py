from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created = serializers.SerializerMethodField(read_only=True)
    liked = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields =['id', 'user', 'body', 'liked', 'created', 'no_of_likes']
    
    def get_created(self, instance):
        return instance.created.strftime('%d-%m-%y')

    def get_liked(self, instance):
        request = self.context.get("request")
        return instance.liked.filter(pk=1).exists()