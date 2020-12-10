# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from stream_control.models import StreamTokenUser , UserStream

# Register your models here.

# ADMIN 
@admin.register(StreamTokenUser)
class StreamTokenUserdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'channel_name',
        'rol_user',
    )
    list_filter = ('id','channel_name')

@admin.register(UserStream)
class UserStreamdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_user',
        'uuid',
    )
    list_filter = ('id','name_user')