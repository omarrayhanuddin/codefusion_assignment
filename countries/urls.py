from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
]
