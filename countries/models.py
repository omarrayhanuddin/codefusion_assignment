from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    cca2 = models.CharField(max_length=2, unique=True)
    capital = models.CharField(max_length=100, blank=True)
    population = models.BigIntegerField()
    timezone = models.CharField(max_length=100)
    flag = models.URLField()
    region = models.CharField(max_length=100)
    languages = models.JSONField()

    def __str__(self):
        return self.name