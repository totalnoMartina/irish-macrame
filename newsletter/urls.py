""" Imports for url rendering and a view """
from django.urls import path
from . import views

urlpatterns = [
    path('newsletter', views.newsletter_sign_up, name='newsletter'),
]
