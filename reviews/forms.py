from django import forms
from django.forms import ModelForm
from .models import Review



class ReviewForm(ModelForm):
    """ A form for the reviews outlook """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_reviewed'].widget = forms.HiddenInput()
        self.fields['user_reviewing'].widget = forms.HiddenInput()

    class Meta:
        model = Review
        fields = '__all__'
