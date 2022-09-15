from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Macrame, Review
from .forms import ReviewForm


def macrames(request):
    """ Rendering products of macrames to be able to manipulate reviews connected to macrames """
    macrame_all = Macrame.objects.all()
    context = {
        'macrame_all': macrame_all,

    }
    return render(request, 'shoppingapp/macrame-detail.html', context)

@login_required
def create_review(request, pk):
    """ Creating a review """
    form = ReviewForm(initial={'product_reviewed': pk, 'user_reviewing': request.user})
    macrame = get_object_or_404(Macrame, pk=pk)
    context = {
        'form': form,
        'macrame': macrame,
    }
    if request.method == 'POST':
        print('Printing Post:', request.POST)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('macrame-detail', macrame_id=pk)

    return render(request, 'reviews/reviews.html', context)


@login_required
def update_review(request, pk):
    """ A view to update review """

    review_ = Review.objects.get(id=pk)
    form = ReviewForm(instance=review_)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review_)
        if form.is_valid():
            form.save()
            return redirect('macrame-detail')

    return render(request, 'reviews/update_reviews.html', context)


@login_required
def delete_review(request, pk):
    """ A view to delete reviews """
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)

    context = {
        # 'form': form,
        'item': review,
    }

    if request.method == 'POST':
        review.delete()
        return redirect('/')

    return render(request, 'reviews/delete_review.html', context)

