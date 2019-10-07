from django.contrib.auth.models import User as UserAuth, Group as GroupAuth
from API.models import User, Country, Group, Sport, Event, City, Comments
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at', 'description', 'age', 'country']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'description', 'country', 'created_at', 'updated_at', 'users']


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['url', 'username', 'email', 'groups']


class GroupsSerializer(serializers.HyperlinkedModelSerializer):
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


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'country']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'users', 'description', 'country', 'city', 'created_at', 'updated_at', 'sport', 'datetime', 'difficulty']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'description', 'country', 'created_at', 'updated_at', 'users']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['user', 'text', 'event', 'created_at', 'updated_at']
