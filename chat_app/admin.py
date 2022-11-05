from django.contrib import admin
from .models import Chat, ChatGroup

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'time_stamp', 'chat_group']

@admin.register(ChatGroup)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']