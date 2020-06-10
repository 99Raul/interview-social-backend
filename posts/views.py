from rest_framework import generics
from .models import Post,Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like_post(self, request, pk=None, *args, **kwargs):
        pk= self.kwargs.get('pk', None)
        user = settings.AUTH_USER_MODEL.objects.get(id=1)
        post = get_object_or_404(Post, pk=pk)
        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer