from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Location):
    star = models.IntegerField()
