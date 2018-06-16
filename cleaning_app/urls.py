# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import Index, Register, Login, CreateCleaningApplication
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^create_cleaning_application/$', CreateCleaningApplication.as_view(), name='create_cleaning_application'),
]
