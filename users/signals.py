from .models import Profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

# sender = user model
# instance = instance of user model
# created = bool
# if created = true, if a new user is created => create a new profile object for a new user!
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(seller=instance)
        
# this is to save the instance of the profile that was just created 
# instance : instance of user model
@receiver(post_save, sender=User)       
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()