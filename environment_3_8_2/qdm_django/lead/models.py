from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from team.models import Team
from patient.models import Patient

class Lead(models.Model):
    WAITING = 'waiting'
    SEEN = 'seen'
    HOLD = 'hold'
    DISPENSED = 'dispensed'
    PAID = 'paid'

    CHOICES_STATUS = (
       (WAITING, 'waiting'),
       (SEEN, 'seen'),
       (HOLD, 'hold'),
       (DISPENSED, 'dispensed'),
       (PAID, 'paid'),
    )

    patient = models.ForeignKey(Patient, related_name='leads', on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(Team, related_name='leads', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.CharField(max_length=250)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=WAITING)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assignedleads', blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='leads', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    