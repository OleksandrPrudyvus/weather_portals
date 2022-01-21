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
    story = models.CharField(max_length=500)

    def __repr__(self):
        return f'{self.name}'
