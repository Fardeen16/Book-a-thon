from django import views
from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("collection/", views.collection, name='collection'),
    path("display/", views.display, name='display'),
    path("saved/", views.display, name='saved')
]
