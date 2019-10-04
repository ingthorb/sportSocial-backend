from django.contrib.auth.models import User as UserAuth, Group as GroupAuth
from API.models import User, Country, Group, Sport, Event
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'events', 'full_name', 'description', 'age', 'country', 'created']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'description', 'country', 'users', 'created']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupAuth
        fields = ['url', 'name']


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['name', 'description']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'users', 'created']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'description', 'country', 'created']
