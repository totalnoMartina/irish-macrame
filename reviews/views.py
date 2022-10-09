""" Imports of modules, models, forms """
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Macrame, Review
from .forms import ReviewForm


def macrames(request):
    """ Rendering products of macrames tacas """
    macrame_all = Macrame.objects.all()
    context = {
        'macrame_all': macrame_all,

    }
    return render(request, 'shoppingapp/macrame-detail.html', context)


@login_required
def create_review(request, pk):
    """ Creating a review """
    form = ReviewForm(initial={'product_reviewed': pk,
                      'user_reviewing': request.user})
    macrame = get_object_or_404(Macrame, pk=pk)
    context = {
        'form': form,
        'macrame': macrame,
    }
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('macrame-detail', macrame_id=pk)

    return render(request, 'reviews/reviews.html', context)


@login_required
def update_review(request, pk):
    """ A view to update review """
    review = Review.objects.get(pk=pk)
    form = ReviewForm(instance=review)
    macrame_id = review.product_reviewed.id

    context = {
        'form': form,
        'review': review,
        'macrame_id': macrame_id
    }
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return HttpResponseRedirect(
                            reverse('macrame-detail',
                            kwargs={'macrame_id': macrame_id}))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return HttpResponseRedirect(
                    reverse('macrame-detail',
                    kwargs={'macrame_id': macrame_id}))
        else:
            messages.error(request,
            'Failed to update review. Please ensure the form is valid.')
    messages.info(request, f'You are editing {review.title}')
    return render(request, 'reviews/update_reviews.html', context)


@login_required
def delete_review(request, pk):
    """ A view to delete reviews """
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)
    macrame_id = review.product_reviewed.id
    context = {
        'form': form,
        'item': review,
        'macrame_id': macrame_id
    }
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return HttpResponseRedirect(
                            reverse('macrame-detail',
                            kwargs={'macrame_id': macrame_id}))

    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect(
                    reverse('macrame-detail',
                    kwargs={'macrame_id': macrame_id}))

    return render(request, 'reviews/delete_review.html', context)
