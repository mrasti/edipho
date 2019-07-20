from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Photo

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('LoginView')
    template_name = 'signup.html'

def photo_list(request):
	if not request.user.is_authenticated:
		return redirect('LoginView')
	queryset = Photo.objects.all().order_by('id')
	return render(request, "photos.html", {"photos": queryset})


def redirect_home(request):
    return redirect('photo_list')

def photo_update(request, pk):
	if not request.user.is_authenticated :
		return redirect('LoginView')
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

