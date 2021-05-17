from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Category, Location, Image

# Create your views here.

def homepage(request):
    images = Image.objects.all()
    return render(request, 'index.html', {"images": images})




