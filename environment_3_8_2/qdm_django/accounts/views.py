"""
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([])
class SFObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        return super(SFObtainAuthToken, self).post(request, *args, **kwargs)

from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import CustomUser
from .serializers import RegisterSerializer, CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
"""
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer, UserTeamSerializer
from .models import CustomUser, UserTeam

class ObtainTokenPairWithDepartmentView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args,**kwargs):
        data = request.data
        new_user = CustomUser.objects.create(
            username=data['username'],
            password=data['password'],
            department=data['department'],
            is_frontstaff=data['is_frontstaff'],
            is_doctor=data['is_doctor'],
            is_backstaff=data['is_backstaff'],
        )
        new_user.save()
        for team in data['userteam']:
            userteam_obj = UserTeam.objects.get(name = team['name'])
            new_user.userteam.add(userteam_obj)
        serializer = CustomUserSerializer(new_user)

        return Response(serializer.data)
'''
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
class UserTeamViewSet(viewsets.ModelViewSet):
    serializer_class = UserTeamSerializer
    def get_queryset(self):
        userteam = UserTeam.objects.all()
        return userteam

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def get_queryset(self):
        customuser = CustomUser.objects.all()
        return customuser
    def create(self, request, *args,**kwargs):
        data = request.data
        new_user = CustomUser.objects.create(
            username=data['username'],
            password=data['password'],
            department=data['department'],
            is_frontstaff=data['is_frontstaff'],
            is_doctor=data['is_doctor'],
            is_backstaff=data['is_backstaff'],
        )
        password = data.pop('password', None)
        new_user.password = make_password(password)
        new_user.save()

        for team in data['userteam']:
            userteam_obj = UserTeam.objects.get(name = team['name'])
            new_user.userteam.add(userteam_obj)
        serializer = CustomUserSerializer(new_user)

        return Response(serializer.data)
