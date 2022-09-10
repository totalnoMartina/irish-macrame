from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('macrames/', views.all_macrames, name='macrames'),
        path('<macrame_id>', views.macrame_detail, name='macrame-detail'),

 
]
