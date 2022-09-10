from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic import View
from .models import Macrame, Category


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


