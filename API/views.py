from API.models import Sport, Event, Comments, Group as Groups, User as Users, City, Country
from API.serializers import SportSerializer, EventSerializer, CommentsSerializer, UsersSerializer, GroupSerializer,GroupsSerializer, CitySerializer, CountrySerializer
from rest_framework import generics
import logging

logger = logging.getLogger(__name__)

class SportList(generics.ListCreateAPIView):
    """
        ---
        get:
            Get list of sports
        post:
            Create a new sport
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        ---
        get:
            Get detailed sport
        put:
            Edit a specific sport
        patch:
            Patch a specific sport
        delete:
            Delete a specific sport
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class EventList(generics.ListCreateAPIView):
    """
        ---
        get:
          Get list of events
        post:
          Create a new event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        ---
        get:
            Get detailed event
        put:
            Edit a specific event
        patch:
            Patch a specific event
        delete:
            Delete a specific event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CommentList(generics.ListCreateAPIView):
    """
        ---
        get:
          Get list of comments
        post:
          Create a new comment
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        ---
        get:
            Get detailed comment
        put:
            Edit a specific comment
        patch:
            Patch a specific comment
        delete:
            Delete a specific comment
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CountryList(generics.ListCreateAPIView):
    """
        ---
        get:
          Get list of countries
        post:
          Create a new country
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        ---
        get:
            Get detailed country
        put:
            Edit a specific country
        patch:
            Patch a specific country
        delete:
            Delete a specific country
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityList(generics.ListCreateAPIView):
    """
        ---
        get:
          Get list of cities
        post:
          Create a new city
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetails(generics.RetrieveUpdateDestroyAPIView):
    """
        ---
        get:
            Get detailed city
        put:
            Edit a specific city
        patch:
            Patch a specific city
        delete:
            Delete a specific city
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UserList(generics.ListCreateAPIView):
    """
        ---
        get:
          Get list of users
        post:
          Create a new user
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDetails(generics.RetrieveUpdateDestroyAPIView):
    """
        ---
        get:
            Get detailed user
        put:
            Edit a specific user
        patch:
            Patch a specific user
        delete:
            Delete a specific user
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class GroupList(generics.ListCreateAPIView):
    """
        ---
        get:
          Get list of groups
        post:
          Create a new group
    """
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer


class GroupsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    """
        ---
        get:
            Get detailed group
        put:
            Edit a specific group
        patch:
            Patch a specific group
        delete:
            Delete a specific group
    """
    def get_queryset(self):
            """
            This view should return a list of all the purchases
            for the currently authenticated user.
            """
            logger.debug('Something went wrong!')

            id = self.request.query_params.get('pk', None)
            logger.debug('Something went wrong!')
            logger.debug(id)
            return Groups.objects.filter(pk=id)
