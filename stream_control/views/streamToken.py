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

from stream_control.serializers import StreamTokenSerializer
from stream_control.models import StreamTokenUser , UserStream
from stream_control.utils import get_tokenrtc

# Create your views here.
import sys
import os
import time
from random import randint
from datetime import datetime

appID = "e72be1261828426ea6d3b5dbad06cea8"
appCertificate = "33e16f3c98c74ab388b3b96224c967ba"
channelName = "canal1"
uid = 2882341555
userAccount = "2882341555"
expireTimeInSeconds = 3600
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expireTimeInSeconds


class StreamTokenViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Users ViewSet"""
    queryset = StreamTokenUser.objects.all()
    serializer_class = StreamTokenSerializer
    lookup_field = 'id_user'

    def get_permissions(self):
        permissions = [AllowAny]
        return [permission() for permission in permissions]

    @action(detail=False, methods=['post'])
    def generate_token(self, request):
        """
            Roles users
            0 = Publisher(Host) default
            1 = Publisher(Host)
            2 = Subscriber(Audience)
            101 = Admin Publisher(Host)
        """

        id_user = int(datetime.now().timestamp())
        token_rtc = get_tokenrtc(
            appID, appCertificate, request.data["channel_name"], id_user,
            request.data["rol_user"], expireTimeInSeconds, currentTimestamp, privilegeExpiredTs
        )

        stream = StreamTokenUser.objects.create(
            channel_name=request.data["channel_name"],
        )


        data = {
            "tokenRTC": token_rtc,
            "uid": id_user
        }
        return Response(data, status=status.HTTP_201_CREATED)

