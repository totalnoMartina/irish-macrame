
"""View to handle 404 page"""
from django.shortcuts import render


def handle_error_404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "error404/page404.html", status=404)
