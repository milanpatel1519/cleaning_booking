# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from .models import Customer, Booking

from django.views import View
register_redirect_url = 'register'


class Index(View):

    def get(self, request):
        return render(request, 'cleaning_app/index.html')


class Login(View):

    def get(self, request):
        """
        Return login template
        """
        form = LoginForm()
        return render(request, 'cleaning_app/login.html', {'form': form})

    def post(self, request):
        """
        login customer and redirect to list of his/her cleaning requests
        """
        errors = {}
        register_form = LoginForm()
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'cleaning_app/login.html', {'errors': errors, 'form': form})
        phone_number = form.cleaned_data.get('phone_number')
        if phone_number:
            customer = Customer.objects.filter(phone_number=phone_number)
            if not customer:
                errors['phone_number'] = "Phone number not registered on our website."
                return render(request, 'cleaning_app/login.html', {'form': register_form, 'errors': errors})
            else:
                booking = Booking.objects.filter(customer=customer)
                return render(request, 'cleaning_app/list_customer_request.html', {'form': register_form, 'booking': booking})
        return render(request, 'cleaning_app/index.html', {'form': register_form})


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


class Logout(View):

    def post(self, request):
        """
        Logout customer form website
        """
        return render(request, 'cleaning_app/index.html')

# def index(request):
#     return render(request, 'cleaning_app/index.html')


# def login(request):
#     return render(request, 'cleaning_app/login.html')


# def register(request):
#     error = {}
#     if request.method == 'POST':
#         register_form = RegisterForm()
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             phone_number = form.cleaned_data.get('phone_number')
#             if phone_number:
#                 customer = Customer.objects.filter(phone_number=phone_number)
#                 if customer:
#                     print "as"
#                     error['phone_number'] = "Already registered Number!"
#                     return render(request, 'cleaning_app/register.html', {'form': register_form, 'errors': error})
#             customer = Customer(
#                 first_name=first_name, last_name=last_name, phone_number=phone_number)
#             customer.save()
#             return render(request, 'cleaning_app/register.html', {'form': register_form, 'error': error})
#     else:
#         register_form = RegisterForm()
#     return redirect('/register')
