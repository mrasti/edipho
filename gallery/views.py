from django.shortcuts import render
from .models import Photo

def photo_list(request):
    queryset = Photo.objects.all()
    return render(request, "photo.html", {"photos": queryset})


# another way to get all objects
# from django.views.generic import ListView
# class PhotoView(ListView):
#     model = Photo
#     template_name = 'photo.html'

