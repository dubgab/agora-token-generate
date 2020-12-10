from django.db import models

class StreamTokenUser(models.Model):
    channel_name = models.CharField("channel name", max_length=100) 
    rol_user = models.PositiveIntegerField("rol user" , default=0)
    def __str__(self):
        """Return username and email"""
        return f'{self.channel_name}'

# Create your models here.
class UserStream(models.Model):
    name_user = models.CharField("name_user", max_length=100) 
    uidd = models.PositiveIntegerField("uuid")
    channel = models.ForeignKey(StreamTokenUser, on_delete=models.CASCADE)
    def __str__(self):
        """Return username and email"""
        return f'{self.name_user}'