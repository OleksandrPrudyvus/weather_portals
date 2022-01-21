"""
Module contains app settings.

Class:
    WeatherConfig(AppConfig)
"""

from django.apps import AppConfig


class WeatherConfig(AppConfig):
    """
    Class is descendant of AppConfig
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
