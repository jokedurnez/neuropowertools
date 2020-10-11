from . import views
from django.urls import path, include
from django.contrib import admin
import django.views.defaults

urlpatterns = [
    path('neuropowerstart', views.neuropowerstart, name = 'neuropowerstart'),
    path('neuropowerFAQ',views.npFAQ,name='npFAQ'),
    path('tutorial',views.tutorial,name='npTutorial'),
    path('methods',views.methods,name='npMethods'),

]
