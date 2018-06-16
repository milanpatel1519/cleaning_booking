# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import Index, Register, Login

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
]
