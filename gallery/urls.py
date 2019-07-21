from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.photo_list, name = 'photo_list'),
    path('photo/add', views.add_photo, name = 'add_photo'),
    path('photo/<int:pk>/update', views.photo_update, name = 'photo_update'),
    path('login/', LoginView.as_view(template_name='login.html'), name= 'LoginView'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name= 'LogoutView'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/profile/', views.redirect_home, name='redirect_home'),
]
