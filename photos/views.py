from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# Create your views here.

def homepage(request):
    return render(request, 'index.html')