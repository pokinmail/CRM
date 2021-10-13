#from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.http import Http404, HttpResponse
'''
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerProfileOrReadOnly

'''
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Team
from accounts.models import CustomUser
from .serializers import UserSerializer, TeamSerializer

class TraceTeam (ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    lookup_url_kwarg = "uid"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        teams = Team.objects.filter(members=uid)
        serializer = TeamSerializer(teams)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
'''
    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user]).first()
   
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()
'''
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_my_team(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)

    return Response(serializer.data)

@api_view(['POST'])
def add_member(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    email = request.data['email']

    print('Email', email)

    user = User.objects.get(username=email)

    team.members.add(user)
    team.save()

    return Response()
'''
class UserProfileListCreateView(ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

@api_view(['POST'])
def add_profile(request):
    user = User.objects.filter(id=request.user.id)
    department = request.data['department']
    is_frontstaff = request.data['is_frontstaff']
    is_doctor = request.data['is_doctor']
    is_backstaff = request.data['is_backstaff']

    print('department', department)
    print('is_frontstaff', is_frontstaff)
    print('is_doctor', is_doctor)
    print('is_backstaff', is_backstaff)

    profile = {user, department, is_frontstaff, is_doctor, is_backstaff}

    user.profile.add(profile)
    user.save()

    return Response()

class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]


class UserCreateUpdateViewSet(viewsets.ModelViewSet):

    serializer_class = UserCreateUpdateSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.save()

@api_view(['POST'])
def post_my_profile(request):
    user = User.objects.filter(id=request.user.id)
    data = request.data
    userprofile = Profile.objects.create(user=user, department=data.department)

    return Response()
'''