from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email=user.email,
            name=user.first_name,
        )
        
        subject = 'welcome to dev search'
        body = 'thank you for siging up. Welcome to our community'

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

# when profile updated user is updated
# this does not update profile when user is updated
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user # can get user from profile. We can also get profile from user because of 1:1 relationship
    if created == False: # this if statement required because we save user when user is saved 2 signals are trigged. without if statement we end up in loop
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# @receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)