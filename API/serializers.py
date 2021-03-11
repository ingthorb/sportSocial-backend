from django.contrib.auth.models import User as UserAuth, Group as GroupAuth
from API.models import User, Country, Group, Sport, Event, City, Comments
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at',
                  'description', 'age', 'country']


class GroupDetailsSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'country', 'created_at', 'updated_at', 'users', 'country_name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    number_of_users = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'country_name', 'description', 'number_of_users']

    @staticmethod
    def get_number_of_users(obj):
        return obj.users.count()


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name', 'description']


class SportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name', 'description']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')

    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'country_name']


class EventSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    city_name = serializers.CharField(source='city.name')
    sports_name = serializers.CharField(source='sport.name')
    number_of_users = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'country', 'country_name', 'city_name',
                  'sports_name', 'datetime', 'difficulty', 'private', 'number_of_users']

    @staticmethod
    def get_number_of_users(obj):
        return obj.users.count()


class EventDetailSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    city_name = serializers.CharField(source='city.name')
    sports_name = serializers.CharField(source='sport.name')
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'users', 'description', 'country', 'country_name', 'city_name', 'sports_name',
                  'city', 'created_at', 'updated_at', 'sport', 'datetime', 'long', 'lat', 'difficulty', 'private']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'text', 'event', 'created_at', 'updated_at']
