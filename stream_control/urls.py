from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'streamToken', StreamTokenViewSet, basename='streamToken')

urlpatterns = [
    path('', include(router.urls))
]
