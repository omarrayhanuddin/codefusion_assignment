from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Country
from django.contrib.auth import get_user_model
User = get_user_model()

class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            name="Test Country",
            cca2="TC",
            capital="Test Capital",
            population=1000000,
            timezone="UTC",
            flag="http://example.com/flag.png",
            region="Test Region",
            languages={"en": "English"}
        )

    def test_country_str(self):
        self.assertEqual(str(self.country), "Test Country")

class CountryViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.country = Country.objects.create(
            name="Test Country",
            cca2="TC",
            capital="Test Capital",
            population=1000000,
            timezone="UTC",
            flag="http://example.com/flag.png",
            region="Test Region",
            languages={"en": "English"}
        )

    def test_country_list_unauthenticated(self):
        response = self.client.get(reverse('country_list'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_country_list_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('country_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_country_list_unauthenticated(self):
        response = self.client.get('/api/countries/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_country_list_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/countries/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)