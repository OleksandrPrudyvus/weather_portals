"""
Module contains all functions working on weather page.

Functions:
    search(request)
    data(request)
"""

from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
import requests
from .models import City
from .forms import CityForm, SelectInfoFromDB
from datetime import datetime
# Create your views here.


def search_city_api(request):
    """
        Function that takes information from the API.
        1) collects information and records it in a database if POST.
        2) showing a page with an input field
    :return: city information template
    """
    appid = '824e405d69ba6bd98c44a3ff6dff1130'
    url = 'https://api.openweathermap.org/' \
          'data/2.5/weather?q={}&appid={}&units=metric'
    form = CityForm()
    if request.method == "POST":
        city_name = request.POST['name']
        res = requests.get(url.format(city_name, appid)).json()
        try:
            form = CityForm(request.POST)
            current_city = City.objects.create(name=res['name'], data=datetime.now().now(), story=res)
            current_city.save()
            weather_info = {
                'name': res['name'],
                'country': res['sys']['country'],
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'feels_like': res['main']['feels_like'],
                'temp_min': res['main']['temp_min'],
                'temp_max': res['main']['temp_max'],
            }
            return render(request, 'weather.html', {'info': weather_info, 'all_info': res, 'form': form})
        except KeyError:
            messages.add_message(request, messages.ERROR, f'City {city_name} not found!')
    return render(request, 'weather.html', {'form': form})


def search_story_into_db(request):
    """
    Function showing story of city(s) into db:
        1) search result by three parameters ['name', 'data_from', 'data_to'] if POST
        2) searches all information about cities in the database
        3) creating paginated list
    :return: template of the list
    """
    form = SelectInfoFromDB()
    info_from_db = City.objects.get_queryset().order_by('id')
    if request.method == 'POST':
        form = SelectInfoFromDB(request.POST)
        if form.is_valid():
            temp = form.cleaned_data
            temp['name'] = temp['name'].capitalize()
            info_from_db = City.objects.raw(
                f"""SELECT * FROM weather_city 
                 WHERE name = '{temp['name']}'
                 and data >= '{temp['data_from']}'
                 and data <= '{temp['data_to']}';""")
        else:
            messages.add_message(request, messages.ERROR, f'City `{request.POST["name"]}` '
                                                          f'from `{request.POST["data_from"]}` '
                                                          f'to `{request.POST["data_to"]}` not found!')
    paginator = Paginator(info_from_db, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'data.html', {'form': form, 'page_obj': page_obj})
