"""Stream views"""
# djangoREST
from rest_framework.views import APIView
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from stream_control.serializers import UserStreamTokenSerializer
from stream_control.models import UserStream
from stream_control.utils import get_tokenrtc

# Create your views here.
import sys
import os
import time
from random import randint
from datetime import datetime

class UserStreamViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Users ViewSet"""
    queryset = UserStream.objects.all()
    serializer_class = UserStreamTokenSerializer
    def get_permissions(self):
        permissions = [AllowAny]
        return [permission() for permission in permissions]

