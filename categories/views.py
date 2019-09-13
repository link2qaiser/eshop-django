from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


# Create your views here.
def index(request):
    categories = Category()
    return render(request, 'categories/list.html', {'list': categories})
