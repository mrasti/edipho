from django.shortcuts import render
from .models import Photo

def photo_list(request):
    queryset = Photo.objects.all().order_by('id')
    return render(request, "photos.html", {"photos": queryset})

def photo_update(request, pk):
    photo = Photo.objects.get(id = pk)
    if request.method == 'POST':
        body = dict(request.POST)
        photo.filter = body['filters'][0]
        photo.save()


# another way to get all objects
# from django.views.generic import ListView
# class PhotoView(ListView):
#     model = Photo
#     template_name = 'photo.html'

