""" Imports of module and views """
from django.urls import path
from . import views


urlpatterns = [
    path('create_review/<int:pk>/', views.create_review, name='create_review'),
    path('update_review/<int:pk>/', views.update_review, name='update_review'),
    path('delete_review/<int:pk>/', views.delete_review, name='delete_review'),
]
