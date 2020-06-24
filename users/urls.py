from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegistrationAPIView
from . import views

urlpatterns = [
    path('users/register', RegistrationAPIView.as_view()),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



# from django.urls import path
# from .views import SignUpView

# urlpatterns = [
#     path('signup', SignUpView.as_view()),
# ]
