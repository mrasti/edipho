from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name = 'photo_list'),
    # path('', views.PhotoView.as_view(), name = 'photo_list'),  <--- for PhotoView in views.py
    
]
