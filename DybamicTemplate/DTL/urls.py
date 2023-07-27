from django.contrib import admin
from django.urls import path
from DTL import views


urlpatterns = [
    path('DTL', views.DTL),
]
