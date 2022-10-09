""" Imports for modules, models, forms """
from django.shortcuts import (render,
             redirect, reverse, get_object_or_404, HttpResponseRedirect)
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Macrame
from .forms import MacrameForm


def index(request):
    """ A view to return homepage """
    return render(request, 'shoppingapp/index.html')


def all_macrames(request):
    """ A view to show all macrame items, including search queries """
    macrames = Macrame.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('macrames'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            macrames = macrames.filter(queries)

    context = {
        'macrames': macrames,
        'search_term': query,
    }
    return render(request, 'shoppingapp/macrames.html', context)


def macrame_detail(request, macrame_id):
    """ A view to show individual product details """

    macrame = get_object_or_404(Macrame, pk=macrame_id)
    context = {
        'macrame': macrame,
    }
    return render(request, 'shoppingapp/macrame-detail.html', context)


class AddLike(LoginRequiredMixin, View):
    """ A class for liking products """
    def post(self, request, pk, *args, **kwargs):
        """ Modifying post method to submit likes """
        macrame = Macrame.objects.get(pk=pk)
        is_like = False
        for like in macrame.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            macrame.likes.add(request.user)
            messages.success(request, 'Thanks for the "Like"!')
        if is_like:
            macrame.likes.remove(request.user)
        next_ = request.POST.get('next_', '/')
        return HttpResponseRedirect(next_)


@login_required
def add_macrame(request):
    """ Add a macrame item to the store """
    if request.method == 'POST':
        form = MacrameForm(request.POST, request.FILES)
        if form.is_valid():
            macrame = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('macrame-detail', args=[macrame.id]))
        else:
            messages.error(request,
            'Failed to add product. Please ensure the form is valid.')
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
    macrame = get_object_or_404(Macrame, pk=macrame_id)
    if request.method == 'POST':
        form = MacrameForm(request.POST, request.FILES, instance=macrame)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Macrame item!')
            return redirect(reverse('macrame-detail', args=[macrame.id]))
        else:
            messages.error(request,
            'Failed updating. Please ensure the form is valid.')
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
    if request.method == 'POST':
        macrame.delete()
        messages.success(request, 'Item deleted!')
        return redirect('home')
    context = {
        'macrame': macrame
    }
    messages.info(request, 'Are you sure?')
    return render(request, 'shoppingapp/delete_macrame.html', context)
