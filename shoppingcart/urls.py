from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shoppingcart, name='view_shoppingcart'),
    path('add/<item_id>/', views.add_to_shoppingcart, name='add_to_shoppingcart'),
    path('adjust/<int:item_id>/', views.adjust_shoppingcart, name='adjust_shoppingcart'),
    path('remove/<int:item_id>/', views.remove_from_shoppingcart, name='remove_from_shoppingcart'),
]
