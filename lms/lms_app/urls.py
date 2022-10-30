# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:19:36 2022

@author: amrma
"""

from django.urls import path
from . import views
urlpatterns=[path('', views.demo, name='demo' ),
             ]