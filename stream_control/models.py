from django.db import models

# Create your models here.

class Stream(models.Model):
    name_room = models.CharField("name_room", max_length=50)   
    is_active =  models.BooleanField("esta activo", default=False)
    def __str__(self):
        """Return username and email"""
        return f'{self.name_room}'

class StreamTokenUser(models.Model):
    channel_name = models.CharField("channel name", max_length=100) 
    rol_user = models.PositiveIntegerField("rol user")
    def __str__(self):
        """Return username and email"""
        return f'{self.name_room}'