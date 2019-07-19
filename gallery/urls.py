from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name = 'photo_list'),
    path('photo/<int:pk>/update', views.photo_update, name = 'photo_update'),
]
