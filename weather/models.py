"""
Module contains class City for DB.

Classes:
    City(models.Model)
"""

from django.db import models
# Create your models here.


class City(models.Model):
    """
    Class is descendant of models.Model.
    It creates table weather_city in db.
    """
    name = models.CharField(max_length=40)
    data = models.DateField(null=True)
    country = models.CharField(max_length=50, null=True)
    temp = models.FloatField(null=True)
    feels_like = models.FloatField(null=True)
    temp_min = models.FloatField(null=True)
    temp_max = models.FloatField(null=True)
    icon = models.CharField(max_length=10, null=True)

    def __repr__(self):
        return f'{self.name}'
