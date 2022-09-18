""" Imports of widgets and module """
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ A model to help replace images from admin side """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'shoppingapp/custom_widget_templates/custom_clearable_file_input.html'
