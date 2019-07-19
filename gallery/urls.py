from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.photo_list, name = 'photo_list'),
    path('photo/<int:pk>/update', views.photo_update, name = 'photo_update'),
    path('login/', LoginView.as_view(template_name='login.html'), name= 'LoginView'),
]
