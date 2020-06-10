from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('comment', views.CommentList.as_view(), name='comment_list'),
]