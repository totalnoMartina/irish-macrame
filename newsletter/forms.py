from django import forms
from django.forms import ModelForm
from .models import NewsletterUser


class NewsletterUserForm(forms.ModelForm):
    """ A form for the signup """

    class Meta:
        model = NewsletterUser()
        fields = '__all__'