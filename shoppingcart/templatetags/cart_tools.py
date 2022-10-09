""" Iport of template """
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculating the subtotal of the shoppingcart """
    return price * quantity
