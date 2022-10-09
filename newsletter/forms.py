""" Import of forms and model """
from django import forms
from .models import NewsletterUser


class NewsletterUserForm(forms.ModelForm):
    """ A form for the signup """

    class Meta:
        """ class to render field inside NewsletterUser """
        model = NewsletterUser
        fields = '__all__'
