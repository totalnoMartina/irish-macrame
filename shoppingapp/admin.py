""" Imports of modules and models """
from django.contrib import admin
from .models import Macrame, Review, Category


class MacrameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('-name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Macrame, MacrameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
