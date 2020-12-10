# rest
from rest_framework import serializers

# models
from stream_control.models import StreamTokenUser

# Task
class StreamTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamTokenUser
        fields = (
            'id',
            'channel_name',
            'rol_user'
        )
