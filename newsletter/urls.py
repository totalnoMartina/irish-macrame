from django.urls import path
from . import views

urlpatterns = [
    path('newsletter', views.newsletter_sign_up, name='newsletter'),
]