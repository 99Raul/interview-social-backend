from rest_framework import routers
# from django.urls import path
# from . import views
from .views import PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls