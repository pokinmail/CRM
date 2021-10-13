from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

class Patient(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    CHOICES_GENDER = (
       (MALE, 'male'),
       (FEMALE, 'female'),
    )

    CHINESE = 'CH'
    ENGLISH = 'EN'
    BOTH = 'BOTH'
    CHOICES_LANGUAGE = (
       (CHINESE, 'Chinese'),
       (ENGLISH, 'English'),
       (BOTH, 'Both'),
    )

    YES = 'Yes'
    NO = 'No'
    CHOICES_YN = (
       (YES, 'Yes'),
       (NO, 'No'),
    )

    engname = models.CharField(max_length=255)
    chiname = models.CharField(max_length=255, blank=True, null=True)
    idnumber = models.CharField(max_length=25, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    tel2 = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    language = models.CharField(max_length=20)
    receipt = models.CharField(max_length=10, choices=CHOICES_YN, default=NO)
    remarks = models.TextField(blank=True, null=True)
    allergy = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='patient', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)  