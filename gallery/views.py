from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'home.html')

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

def search_results(request):
 
    if 'image'in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_location_id(search_term)
        message = f"{search_term}"

    elif 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category_id(search_term)
        message = f"{search_term}"

        return render(request, '',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search m',{"message":message})
