from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location

# Create your views here.
def index(request):

    title = "Pixels"
    images = Image.objects.all()
    print(images)
    
    locations = Location.display_all_locations()
    return render(request, "index.html", {"title": title, "images":images, "locations":locations})

def search_results(request):
    '''
    Displays the results search page of images in specific categories
    '''
    if 'image'in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'img-gallery/category.html',{"message":message,"images": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'img-gallery/search.html',{"message":message})

def search_location(request):
    '''
    Displays the various locations of the images
    '''
    if 'image'in request.GET and request.GET["image"]:
        location_term = request.GET.get("image")
        searched_location = Image.filter_by_location(location_term)
        message = f"{location_term}"

        return render(request,'img-gallery/location.html',{"message":message,"images": searched_location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'img-gallery/search.html',{"message":message})

