from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser, UserTeam

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password', 'password1', 'department', 'is-frontstaff', 'is_doctor', 'is_backstaff', 'userteam')
        depth =1

    def validate(self,attr):
        validate_password(attr['password'])
        return attr

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],\
            department=validated_data['department'],
            is_frontstaff=validated_data['is_frontstaff'],
            is_doctor=validated_data['is_doctor'],
            is_backstaff=validated_data['is_backstaff'],
            userteam=validated_data['userteam']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = ('id', 'name')

class CustomUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'department', 'is_frontstaff', 'is_doctor', 'is_backstaff', 'userteam')
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['department'] = user.department
        return token