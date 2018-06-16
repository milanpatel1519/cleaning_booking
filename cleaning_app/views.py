# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import RegisterForm, LoginForm, CreateCleaningApplicationForm
from .models import Customer, Booking, Cities, Cleaner

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
        login_form = LoginForm()
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'cleaning_app/login.html', {'errors': errors, 'form': form})
        phone_number = form.cleaned_data.get('phone_number')
        if phone_number:
            customer = Customer.objects.filter(phone_number=phone_number)
            if not customer:
                errors['phone_number'] = "Phone number not registered on our website."
                return render(request, 'cleaning_app/login.html', {'form': login_form, 'errors': errors})
            else:
                booking = Booking.objects.filter(customer=customer)
                request.session.update({'customer': customer.values()[0]})
                return render(request, 'cleaning_app/list_customer_request.html', {'form': login_form, 'booking': booking, 'customer': customer.values() and customer.values()[0]})
        return render(request, 'cleaning_app/index.html', {'form': login_form})


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


class CreateCleaningApplication(View):

    def get(self, request):
        """
        Return to schedule cleaning application
        """
        create_cleaning_application_form = CreateCleaningApplicationForm()
        return render(request, 'cleaning_app/create_cleaning_application.html', {'form': create_cleaning_application_form})

    def post(self, request):
        """
        redirect to listing page if cleaner available and if not then please show message
        """
        errors = {}
        login_form = LoginForm()
        form = CreateCleaningApplicationForm(request.POST)
        if not form.is_valid():
            return render(request, 'cleaning_app/create_cleaning_application.html', {'errors': errors, 'form': form})
        city = form.cleaned_data.get('city')
        date = form.cleaned_data.get('date')
        customer = request.session.values()[0]['id']
        customer = Customer.objects.get(id=customer)
        customer_dict = {}
        customer_dict['first_name'] = customer.first_name
        customer_dict['last_name'] = customer.last_name
        if city and date:
            booking = Booking.objects.filter(city=city, date=date)
            if booking:
                errors['error'] = "That time we can not schedule cleaning appointment!"
                errors['success'] = ""
                booking = Booking.objects.filter(customer=customer)
                return render(request, 'cleaning_app/list_customer_request.html', {'form': login_form, 'booking': booking, 'errors': errors, 'customer': customer_dict})
        cities = Cities.objects.get(id=city)
        try:
            cleaner = Cleaner.objects.get(city=[city])
        except:
            errors['error'] = "No cleaner available in that city."
            errors['success'] = ""
            booking = Booking.objects.filter(customer=customer)
            return render(request, 'cleaning_app/list_customer_request.html', {'form': login_form, 'booking': booking, 'errors': errors, 'customer': customer_dict})
        if not cleaner:
            errors['error'] = "No cleaner assigned for that city."
            errors['success'] = ""
            booking = Booking.objects.filter(customer=customer)
            return render(request, 'cleaning_app/list_customer_request.html', {'form': login_form, 'booking': booking, 'errors': errors, 'customer': customer_dict})
        booking = Booking(city=cities, date=date, customer=customer, cleaner=cleaner)
        booking.save()
        booking = Booking.objects.filter(customer=customer)
        errors['success'] = "We have successfully scheduleed your cleaning appointment!"
        errors['error'] = ""
        return render(request, 'cleaning_app/list_customer_request.html', {'form': login_form, 'booking': booking, 'errors': errors, 'customer': customer_dict})


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
