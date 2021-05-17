from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Category, Location, Image

# Create your views here.

def homepage(request):
    images = Image.objects.all()
    return render(request, 'index.html', {"images": images})

def view_image(request, image_id):
    image = Image.get_image_by_id(image_id)
    return render(request, 'view.html', {"image": image})

def search_categories(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search_categories.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search_categories.html', {"message": message})

def search_locations(request):
    if 'city' in request.GET and request.GET["city"]:
        search_term = request.GET.get("city")
        searched_images = Image.filter_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'search_locations.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any city"
        return render(request, 'search_locations.html', {"message": message})
