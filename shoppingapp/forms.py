""" Imports of modules, models and widgets """
from django import forms
from .models import Macrame, Category
from .widgets import CustomClearableFileInput


class MacrameForm(forms.ModelForm):
    """ A form for macrame items """
    class Meta:
        """ A class to render all fields """
        model = Macrame
        fields = '__all__'

    image = forms.ImageField(label='image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
