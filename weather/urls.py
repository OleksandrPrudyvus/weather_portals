from django.urls import path
from . import views


urlpatterns = [
    path('', views.search_city_api, name='home'),
    path('data', views.search_story_into_db, name='data')
]
