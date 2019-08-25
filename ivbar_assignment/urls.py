"""ivbar_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from events.views import EventView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', EventView.as_view({'get':'list'})),
    path('caregivers/<int:caregiver_id>/events/', EventView.as_view({'post':'create'})),
]
