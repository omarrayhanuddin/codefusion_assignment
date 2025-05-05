from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = [
            "url",
            "id",
            "name",
            "cca2",
            "capital",
            "population",
            "timezone",
            "flag",
            "region",
            "languages",
        ]
