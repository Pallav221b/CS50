
from django import views

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("pallav", views.pallav, name="pallav"),
    path("dubey", views.dubey, name="dubey"),
    
]