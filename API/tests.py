from django.test import TestCase
from .models import User, Country
# Create your tests here.


class UserModelTests(TestCase):
    def setUp(self):
        country = Country.objects.create(name="test")
        User.objects.create(username='ingthor', country=country, age=10)

    def test_created_user(self):
        user = User.objects.get(username='ingthor')
        self.assertEqual(user.username, 'ingthor')