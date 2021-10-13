#from django.contrib.auth.models import User
from django.shortcuts import render


from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Patient
from .serializers import PatientSerializer

from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class PatientPagination(PageNumberPagination):
    page_size = 10

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    pagination_class = PatientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id','engname','chiname','idnumber','dob','address','tel','tel2',)

    def perform_create(self, serializer):
        patient = serializer.save(created_by=self.request.user)
        #patient.save()


