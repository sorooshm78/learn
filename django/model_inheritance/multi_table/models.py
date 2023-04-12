from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} - {self.address}"


class Restaurant(Location):
    star = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.address} - {self.star}"
