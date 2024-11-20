from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    profile_img = models.ImageField(blank=True, null=True, upload_to='profiles/', default='profiles/user_d.jpg')
    social_github = models.CharField(null=True, blank=True, max_length=200)
    social_linkedIn = models.CharField(null=True, blank=True, max_length=200)
    social_youtube = models.CharField(null=True,blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
   

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,blank=True)
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject