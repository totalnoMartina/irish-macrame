""" Imports of modules and model """
from django.contrib import admin
from .models import NewsletterUser


@admin.register(NewsletterUser)
class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('email_user', )
    fields = ('email_user', )

