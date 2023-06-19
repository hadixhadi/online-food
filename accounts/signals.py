
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from.models import *

@receiver(post_save,sender=User) 
def post_save_user_profile_created(sender,instance,created,**kwargs):
    if created: # 'created' is a flag that will be true when User crated
        UserProfile.objects.create(user=instance)
    else:
        try: #if user update this will profile update too
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except: #if super user update it will create a profile 
            UserProfile.objects.create(user=instance)
           