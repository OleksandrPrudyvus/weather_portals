"""
Module contains class CityForm and SelectInfoFromDB for Forms.

Classes:
     CityForm(ModelForm)
      SelectInfoFromDB(forms.Form)
"""

from .models import City
from django.forms import ModelForm, TextInput, DateInput


from django import forms


class CityForm(ModelForm):
    """
    Class is descendant of ModelForm.
    It creates form from City model in db.
    """
    name = forms.CharField(required=False)

    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'id': "city",
                                            'placeholder': "City",
                                            'aria-label': "Search",
                                            'name': "city",
                                            'aria-describedby': "search-addon"
                                            })}


class SelectInfoFromDB(forms.Form):
    """
    Class is descendant of forms.Form.
    It creates a search form in the db.
    """
    name = forms.CharField(required=False, max_length=40, widget=TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': "City name: ",
                                                                  'type': "text",
                                                                  }))
    data_from = forms.DateField(required=False, widget=DateInput(attrs={'class': 'form-control datepicker',
                                                        'placeholder': "Data from: yyyy-mm-dd ",
                                                        'type': "text",
                                                        'id': "data_from"
                                                                  }))
    data_to = forms.DateField(required=False, widget=DateInput(attrs={'class': 'form-control datepicker',
                                                      'placeholder': "Data to: yyyy-mm-dd",
                                                      'type': "text",
                                                      'id': "data_to",
                                                                  }))
