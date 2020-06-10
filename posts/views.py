from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like_post(self, request, pk=None, *args, **kwargs):
        pk= self.kwargs.get('pk', None)
        user = User.objects.get(id=1)
        post = get_object_or_404(Post, pk=pk)
        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)