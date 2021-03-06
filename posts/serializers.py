from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    # created = serializers.SerializerMethodField(read_only=True)
    # liked = serializers.SerializerMethodField(read_only=True)
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields =['id', 'user', 'body', 'liked', 'created', 'no_of_likes','title','comments',]
    
    def get_created(self, instance):
        return instance.created.strftime('%d-%m-%y')

    def get_liked(self, instance,):
        request = self.context.get("request")
        return instance.liked.all().exists()
        # return instance.liked.filter(pk=1).exists()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =['user', 'post', 'body','id','created','updated',] 
