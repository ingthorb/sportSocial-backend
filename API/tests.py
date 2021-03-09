from rest_framework.test import APITestCase
from API.models import Sport, Country, City


class SportViewTestCase(APITestCase):

    def setUp(self):
        self.sport_name = 'Football'
        self.description = 'Play with your feet'

    def test_create_sport(self):
        """
            Ensure we can create a new Sport object.
        """
        data = {'name': self.sport_name,
                'description': self.description }
        response = self.client.post("/sports/", data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(Sport.objects.count(), 1)
        self.assertEqual(Sport.objects.get().name, self.sport_name)


class CountryViewTestCase(APITestCase):

    def setUp(self):
        self.country_name = 'Switzerland'

    def test_create_country(self):
        """
            Ensure we can create a new country object.
        """
        data = {'name': self.country_name}
        response = self.client.post("/countries/", data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.get().name, self.country_name)
