from django import forms
from .models import Photo, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'picture', 'default_color',)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'location', 'image',)
