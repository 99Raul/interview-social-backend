from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
# from .views import PostViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)


# urlpatterns = router.urls + [
#     path('comment', views.CommentList.as_view(), name='comment_list'),
#     path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
# ]

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('comments/', views.CommentList.as_view(), name='comments_list'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]


# path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
# path('comment', views.CommentList.as_view(), name='comment_list'),
