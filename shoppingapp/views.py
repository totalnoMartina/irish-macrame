from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.views.generic import View
from .models import Macrame, Category
from .forms import MacrameForm


def index(request):
    """ A view to return homepage """
    return render(request, 'shoppingapp/index.html')


def all_macrames(request):
    """ A view to show all macrame items, including sorting and search queries """

    macrames = Macrame.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                macrames = macrames.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            macrames = macrames.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            macrames = macrames.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('macrames'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            macrames = macrames.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'macrames': macrames,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'shoppingapp/macrames.html', context)


def macrame_detail(request, macrame_id):
    """ A view to show individual product details """

    macrame = get_object_or_404(Macrame, pk=macrame_id)

    context = {
        'macrame': macrame,
    }

    return render(request, 'shoppingapp/macrame-detail.html', context)


@login_required
def add_macrame(request):
    """ Add a macrame item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = MacrameForm(request.POST, request.FILES)
        if form.is_valid():
            macrame = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('macrame-detail', args=[macrame.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = MacrameForm()
        
    template = 'shoppingapp/add_macrames.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_macrame(request, macrame_id):
    """ Edit a macrame item in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    macrame = get_object_or_404(Macrame, pk=macrame_id)
    if request.method == 'POST':
        form = MacrameForm(request.POST, request.FILES, instance=macrame)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('macrame-detail', args=[macrame.id]))
        else:
            messages.error(request, 'Failed to update item. Please ensure the form is valid.')
    else:
        form = MacrameForm(instance=macrame)
        messages.info(request, f'You are editing {macrame.name}')

    template = 'shoppingapp/edit_macrame.html'
    context = {
        'form': form,
        'macrame': macrame,
    }

    return render(request, template, context)


@login_required
def delete_macrame(request, macrame_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    macrame = get_object_or_404(Macrame, pk=macrame_id)
    macrame.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('macrames'))