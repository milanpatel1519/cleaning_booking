# -*- coding: utf-8 -*-
from django import forms
from .models import Cities
from django.utils.functional import lazy
from datetime import datetime


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=10, required=False)


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=10, required=False)


def CHOICES():
    choices = []
    for city in Cities.objects.all():
        choices.append(((city.id), str(city.name)))
    choices = (choices)
    return choices


class CreateCleaningApplicationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CreateCleaningApplicationForm, self).__init__(*args, **kwargs)
        self.__class__.declared_fields.get('city').choices = \
            lazy(CHOICES, list)()

    city = forms.ChoiceField(label="City", widget=forms.Select(), required=True)
    date = forms.DateTimeField(initial=datetime.now(), required=True)
