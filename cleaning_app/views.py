# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import RegisterForm
from .models import Customer

from django.views import View
register_redirect_url = 'register'


class Index(View):

    def get(self, request):
        return render(request, 'cleaning_app/index.html')


class Login(View):

    def get(self, request):
        return render(request, 'cleaning_app/index.html')


class Register(View):

    def get(self, request):
        """
        Return registeration template
        """
        form = RegisterForm()
        return render(request, 'cleaning_app/register.html', {'form': form})

    def post(self, request):
        """
        registeration customer and redirect to index page
        """
        errors = {}
        register_form = RegisterForm()
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'cleaning_app/register.html', {'errors': errors, 'form': form})
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone_number = form.cleaned_data.get('phone_number')
        if phone_number:
            customer = Customer.objects.filter(phone_number=phone_number)
            if customer:
                errors['phone_number'] = "Already registered Number!"
                return render(request, 'cleaning_app/register.html', {'form': register_form, 'errors': errors})
        customer = Customer(
            first_name=first_name, last_name=last_name, phone_number=phone_number)
        customer.save()
        return render(request, 'cleaning_app/index.html', {'form': register_form})
