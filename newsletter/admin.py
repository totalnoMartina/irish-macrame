""" Imports of modules and model """
from django.contrib import admin
from .models import NewsletterUser


admin.site.register(NewsletterUser)
