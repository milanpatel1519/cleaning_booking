# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from django.utils.functional import lazy


class Cities(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __unicode__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    phone_number = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return self.first_name


class Booking(models.Model):
    customer = models.ForeignKey('Customer',
                                 on_delete=models.CASCADE)
    cleaner = models.ForeignKey('Cleaner',
                                on_delete=models.CASCADE)
    city = models.ForeignKey('Cities',
                             on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, blank=False, null=False)

    def __unicode__(self):
        return self.customer.first_name


def CHOICES():
    choices = []
    for city in Cities.objects.all():
        choices.append(((city.id), str(city.name)))
    choices = (choices)
    return choices


class Cleaner(models.Model):

    def __init__(self, *args, **kwargs):
        super(Cleaner, self).__init__(*args, **kwargs)
        self._meta.get_field('city').choices = \
            lazy(CHOICES, list)()

    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    quality_score = models.FloatField(blank=False, validators=[
                                      MinValueValidator(0.0), MaxValueValidator(5.0)])
    city = MultiSelectField(max_length=10)

    def __unicode__(self):
        return self.first_name
