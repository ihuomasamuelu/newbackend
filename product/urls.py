from django.urls import path
from.views import allfood, createfood

urlpatterns = [
    path("allfood/",allfood),
    path("createfood/", createfood),
]


