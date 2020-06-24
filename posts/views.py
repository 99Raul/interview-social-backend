from rest_framework import generics, permissions
from rest_framework import viewsets
from .models import Post,Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model
# from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated
# Create your views here.

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = [IsAuthenticated]


#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     @action(detail=True, methods=['post'])
#     def like_post(self, request, pk=None, *args, **kwargs, ):
#         pk= self.kwargs.get('pk', None)
#         user = settings.AUTH_USER_MODEL.objects.get(id=id)
#         #  user = settings.AUTH_USER_MODEL.objects.get(id=1)
#         post = get_object_or_404(Post, pk=pk)
#         if user in post.liked.all():
#             post.liked.remove(user)
#         else:
#             post.liked.add(user)
#         post.save()
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (permissions.AllowAny, )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]