# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Customer, Booking, Cleaner, Cities

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Cleaner)
admin.site.register(Cities)
