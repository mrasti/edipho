from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Photo, Profile
from .forms import PhotoForm, ProfileForm
import simplejson as json

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('LoginView')
    template_name = 'signup.html'

def photo_list(request):
	if not request.user.is_authenticated:
		return redirect('LoginView')
	queryset = Photo.objects.filter(creator = request.user).order_by('id')
	return render(request, "photos.html", {"photos": queryset, "profile": get_profile(request), "editable": True})

def user_page(request, pk):
	if not request.user.is_authenticated:
		return redirect('LoginView')
	queryset = Photo.objects.filter(creator = pk).order_by('id')
	return render(request, "photos.html", {"photos": queryset, "profile": get_profile(request), "editable": False})

def discover(request):
	if not request.user.is_authenticated :
		return redirect('LoginView')
	return render(request, 'discover.html', {'users': Profile.objects.all().exclude(user = request.user), "profile": get_profile(request)})

def add_photo(request):
	if not request.user.is_authenticated:
		return redirect('LoginView')

	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.creator = request.user
			form.save()
			return HttpResponseRedirect(reverse_lazy('photo_list'))
		else:
			return HttpResponseRedirect(json.dumps(form.errors))
	else:
		form = PhotoForm()
		return render(request, 'add_photo.html', {'form': form})


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
	
def edit_profile(request):
	if not request.user.is_authenticated :
		return redirect('LoginView')

	profile = get_profile(request)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('photo_list'))
		else:
			return HttpResponseRedirect(json.dumps(form.errors))
	else:
		form = ProfileForm(instance=profile)
		return render(request, 'edit_profile.html', {'form': form})


def get_profile(request):
	profile = Profile.objects.filter(user=request.user).first()
	if profile == None:
		profile = Profile(user=request.user, name=request.user.username)
		profile.save()
	return profile

def home_page(request):
	return discover(request)

# another way to get all objects
# from django.views.generic import ListView
# class PhotoView(ListView):
#     model = Photo
#     template_name = 'photo.html'

