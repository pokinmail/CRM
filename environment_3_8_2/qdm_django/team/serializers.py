#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Team
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "department",
            "is_frontstaff",
            "is_doctor",
            "is_backstaff",
        )

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
            "created_by",
        )


'''
class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = (
            "department",
            "is_frontstaff",
            "is_doctor",
            "is_backstaff",
        )

class UserCreateUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )

    def to_representation(self, instance):
        data = super(UserCreateUpdateSerializer, self).to_representation(instance)
        profile = data.pop('profile')
        for key, val in profile.items():
            data.update({key: val})
        return data
'''