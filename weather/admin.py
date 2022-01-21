"""
Module contains admin settings.
"""

from django.contrib import admin
from .models import City

# Register City models.
admin.site.register(City)
