# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Customer(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    phone_number = models.CharField(blank=False, max_length=100)


class Booking(models.Model):
    customer = models.CharField(blank=False, max_length=100)
    cleaner = models.CharField(blank=False, max_length=100)
    date = models.DateTimeField(blank=False)


class Cleaner(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    quality_score = models.FloatField(blank=False, validators=[
                                      MinValueValidator(0.0), MaxValueValidator(5.0)])
