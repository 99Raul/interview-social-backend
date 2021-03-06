from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('profile', views.ProfileList.as_view(), name='profile_list'),
    path('profile/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
]