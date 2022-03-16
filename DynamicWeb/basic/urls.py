from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first),
    path('page',views.second),
    path('data',views.third)
]