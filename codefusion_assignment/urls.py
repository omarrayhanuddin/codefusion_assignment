from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from countries import views as country_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("countries.urls")),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="countries/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", country_views.register, name="register"),
]
