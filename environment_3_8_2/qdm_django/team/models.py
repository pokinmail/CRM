#from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
#from django.db.models.signals import post_save
#from django.dispatch import receiver

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)  
'''
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True, null=True)   
    is_frontstaff = models.BooleanField(default= False)
    is_doctor = models.BooleanField(default= False)
    is_backstaff = models.BooleanField(default= False)
    
    def __str__(self):
        return 'user {}'.format(self.user.username)

# Receiver function, automatically called whenever a new User instance is created

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Receiver function, automatically called whenever the User instance is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''