from django.shortcuts import render
from django.views.generic import TemplateView


def home_view(request):
    """Home page to test site functionality."""
    return render(request, 'generic/home.html')


def blog_view(request):
    """Blog page to test site functionality."""
    return render(request, 'generic/under_construction.html')