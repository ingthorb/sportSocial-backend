from rest_framework.test import APITestCase
from API.models import User, Country
from API.serializers import UserSerializer

class UserModelTests(APITestCase):
    def setUp(self):
        self.country = Country.objects.create(name='Switzerland')
        User.objects.create(username='ingthor', age=10, country=self.country)

    def test_created_user(self):
        user = User.objects.get(username='ingthor')
        self.assertEqual(user.username, 'ingthor')