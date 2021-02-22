from django.contrib.auth.models import User as UserAuth, Group as GroupAuth
from API.models import User, Country, Group, Sport, Event, City, Comments
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at', 'description', 'age', 'country']


class GroupSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    class Meta:
        model = Group
        fields = ['name', 'description', 'country', 'created_at', 'updated_at', 'users', 'country_name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['url', 'username', 'email', 'groups']


class GroupsSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
# Add users
    class Meta:
        model = GroupAuth
        fields = ['name', 'country_name','description']


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['name', 'description']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    class Meta:
        model = City
        fields = ['name', 'country', 'country_name']


class EventSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    city_name = serializers.CharField(source='city.name')
    sports_name = serializers.CharField(source='sport.name')
# Add users
    class Meta:
        model = Event
        fields = ['name', 'users', 'description', 'country','country_name','city_name','sports_name', 'city', 'created_at', 'updated_at', 'sport', 'datetime', 'long', 'lat', 'difficulty', 'private']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['user', 'text', 'event', 'created_at', 'updated_at']
