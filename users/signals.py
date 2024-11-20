from django.db.models.signals import post_save,post_delete, pre_delete
from .models import Profile
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings

# from django.dispatch import receiver

 
# @receiver(post_save, sender=Profile)



# This is for when user is created then profile is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            email = user.email
        )


        subject = 'Welcome to Django My Projects'
        message = 'We are glad you are here!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )
post_save.connect(create_profile, sender=User)



# This is for when profile is deleted then also User is delete
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
post_delete.connect(delete_profile, sender=Profile)


# def delete_user(sender, instance, **kwargs):
#     user = instance.profile
#     user.delete()
# pre_delete.connect(delete_user, sender=User)





# this is for when user edit thats profile then also update user details

def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.email = profile.email
        user.save()

post_save.connect(updateProfile, sender=Profile)
