from django.shortcuts import render

def index(request):
    """ A view to return homepage """
    return render(request, 'shoppingapp/index.html')
