""" Main urls for the apps to be connected """
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handle_error_404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('shoppingapp.urls')),
    path('reviews/', include('reviews.urls')),
    path('shoppingcart/', include('shoppingcart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('newsletter/', include('newsletter.urls')),
]

handler404 = 'makemacrame.views.handle_error_404'
