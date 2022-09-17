from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsletterUserForm


def newsletter_sign_up(request):
    """ A view to render email signup option """
    if request.method == POST:
        form = NewsletterUserForm(request.POST)
        if form.is_valid(:
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect('home')


        
        
    return render(request, 'newsletter/newsletter.html')
        
