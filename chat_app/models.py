from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    content = models.CharField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now=True)
    chat_group = models.ForeignKey('ChatGroup', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ChatGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name