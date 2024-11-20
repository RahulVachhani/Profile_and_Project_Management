from django.contrib import admin
from .models import Profile, Skill, Message

# Register your models here.

class ProfileShow(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

class MessageShow(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'subject']

admin.site.register(Profile, ProfileShow)
admin.site.register(Skill)
admin.site.register(Message, MessageShow)
