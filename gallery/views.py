from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def index(request):
    return render(request, 'home.html')

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"img-gallery/image.html", {"image":image})

def search_results(request):
    '''
    Displays the results search page
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
        search_term = request.GET.get("image")
        searched_location = Image.search_by_location(search_term)
        message = f"{search_term}"

        return render(request,'img-gallery/location.html',{"message":message,"images": searched_location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'img-gallery/search.html',{"message":message})

