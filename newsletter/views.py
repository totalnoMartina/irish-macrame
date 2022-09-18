""" Imports of form, model and modules needed """
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsletterUserForm


def newsletter_sign_up(request):
    """ A view to render email signup option """
    if request.method == "POST":
        email = request.POST['email']
        print(email)
        messages.success(request, "Email received. thank You! ")
        return redirect('home')

    return render(request, "newsletter/newsletter.html")
