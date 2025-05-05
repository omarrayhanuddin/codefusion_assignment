from django.core.management.base import BaseCommand
import requests
from countries.models import Country
from decouple import config

class Command(BaseCommand):
    help = 'Fetch and store country data from REST Countries API'

    def handle(self, *args, **kwargs):
        api_url = config('REST_COUNTRIES_API_URL', default='https://restcountries.com/v3.1/all')
        response = requests.get(api_url)
        if response.status_code == 200:
            countries = response.json()
            for country in countries:
                Country.objects.update_or_create(
                    cca2=country.get('cca2'),
                    defaults={
                        'name': country.get('name', {}).get('common', ''),
                        'capital': ', '.join(country.get('capital', [''])),
                        'population': country.get('population', 0),
                        'timezone': ', '.join(country.get('timezones', [''])),
                        'flag': country.get('flags', {}).get('png', ''),
                        'region': country.get('region', ''),
                        'languages': country.get('languages', {})
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully fetched and stored country data'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch country data'))
