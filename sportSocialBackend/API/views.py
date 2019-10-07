from rest_framework import viewsets
from API.models import Sport, Event, Comments, Group as Groups, User as Users, City, Country
from API.serializers import UserSerializer, GroupSerializer, SportSerializer, EventSerializer, CommentsSerializer, UsersSerializer, GroupsSerializer, CitySerializer, CountrySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def sport_list(request):
    """
    :param request:
    :return: List of sports available or created
    """
    if request.method == 'GET':
        sports = Sport.objects.all().only('description')
        data = SportSerializer(sports, many=True, fields='name').data
        return Response(data)

    elif request.method == 'POST':
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sport_detail(request, id):
    """
    :param id: Id of the sport
    :param request:
    :return: Details of specific sport, edit or delete
    """

    try:
        sport = Sport.objects.get(id=id)
    except Sport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = SportSerializer(sport).data
        return Response(data)

    elif request.method == 'PUT':
        serializer = SportSerializer(sport)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def event_list(request):
    """
    :param request:
    :return: List of events or create
    """
    if request.method == 'GET':
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
