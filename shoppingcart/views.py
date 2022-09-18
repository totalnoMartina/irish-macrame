""" Imports of modules, model and messages """
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from shoppingapp.models import Macrame


def view_shoppingcart(request):
    """ A view that renders the bag contents page """

    return render(request, 'shoppingcart/shoppingcart.html')


def add_to_shoppingcart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    macrame = Macrame.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'macrame_size' in request.POST:
        size = request.POST['macrame_size']
    shoppingcart = request.session.get('shoppingcart', {})

    if size:
        if item_id in list(shoppingcart.keys()):
            if size in shoppingcart[item_id]['items_by_size'].keys():
                shoppingcart[item_id]['items_by_size'][size] += quantity
            else:
                shoppingcart[item_id]['items_by_size'][size] = quantity
        else:
            shoppingcart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(shoppingcart.keys()):
            shoppingcart[item_id] += quantity
        else:
            shoppingcart[item_id] = quantity
            messages.success(request,
            f'Added {macrame.name} to your shopping cart')

    request.session['shoppingcart'] = shoppingcart
    return redirect(redirect_url)


def adjust_shoppingcart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'macrame_size' in request.POST:
        size = request.POST['macrame_size']
    shoppingcart = request.session.get('shoppingcart', {})

    if size:
        if quantity > 0:
            shoppingcart[item_id]['items_by_size'][size] = quantity
        else:
            del shoppingcart[item_id]['items_by_size'][size]
            if not shoppingcart[item_id]['items_by_size']:
                shoppingcart.pop(item_id)
    else:
        if quantity > 0:
            shoppingcart[item_id] = quantity
        else:
            shoppingcart.pop(item_id)

    request.session['shoppingcart'] = shoppingcart
    return redirect(reverse('view_shoppingcart'))


def remove_from_shoppingcart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        size = None
        if 'macrame_size' in request.POST:
            size = request.POST['macrame_size']
        shoppingcart = request.session.get('shoppingcart', {})

        if size:
            del shoppingcart[item_id]['items_by_size'][size]
            if not shoppingcart[item_id]['items_by_size']:
                shoppingcart.pop(item_id)
        else:
            shoppingcart.pop(item_id)

        request.session['shoppingcart'] = shoppingcart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
