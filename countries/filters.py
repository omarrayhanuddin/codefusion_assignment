import django_filters
from .models import Country


class CountryFilter(django_filters.FilterSet):
    region = django_filters.CharFilter(lookup_expr="icontains", label="Region")
    name = django_filters.CharFilter(lookup_expr="icontains", label="Name")
    language = django_filters.CharFilter(method="filter_language", label="Language")

    class Meta:
        model = Country
        fields = ["region", "language", "name"]

    def filter_language(self, queryset, name, value):
        return queryset.filter(languages__has_key=value)
