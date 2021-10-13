from django.db import models
from django.contrib.auth.models import AbstractUser

class UserTeam(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class CustomUser(AbstractUser):
    department = models.CharField(max_length=100, blank=True, null=True)   
    is_frontstaff = models.BooleanField(default= False)
    is_doctor = models.BooleanField(default= False)
    is_backstaff = models.BooleanField(default= False)
    userteam = models.ManyToManyField(UserTeam)
