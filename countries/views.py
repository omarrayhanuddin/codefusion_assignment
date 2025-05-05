from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Country
from .serializers import CountrySerializer
from .filters import CountryFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filterset_class = CountryFilter


@login_required
def country_list(request):
    search_query = request.GET.get("search", "")
    region_query = request.GET.get("region", "")
    language_query = request.GET.get("language", "")

    countries = Country.objects.all()

    if search_query:
        countries = countries.filter(name__icontains=search_query)

    if region_query:
        countries = countries.filter(region__icontains=region_query)

    if language_query:
        countries = countries.filter(languages__has_key=language_query)

    return render(request, "countries/country_list.html", {"countries": countries})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return render(request, "countries/registration.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "countries/registration.html")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Registration successful. Please login.")
        login(request, user)
        return redirect("country_list")

    return render(request, "countries/registration.html")
