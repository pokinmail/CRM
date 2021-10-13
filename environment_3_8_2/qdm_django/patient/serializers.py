from rest_framework import serializers
from .models import Patient
from team.serializers import UserSerializer

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        read_only_fields = (
            'created_by',
            'created_at',
        ),
        fields = (
            'id',
            'engname',
            'chiname',
            'idnumber',
            'dob',
            'address',
            'tel',
            'tel2',
            'gender',
            'language',
            'receipt',
            'remarks',
            'allergy',
        )