from django.contrib import admin
from django.urls import path, include
from career import views

urlpatterns = [
    path('', views.career, name='career'),
]
