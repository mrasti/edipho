from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('user/<int:pk>', views.user_page, name = 'user_page'),
    path('discover/', views.discover, name = 'discover'),
    path('gallery/', views.photo_list, name = 'photo_list'),
    path('photo/add', views.add_photo, name = 'add_photo'),
    path('photo/<int:pk>/update', views.photo_update, name = 'photo_update'),
    path('login/', LoginView.as_view(template_name='login.html'), name= 'LoginView'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name= 'LogoutView'),
    path('profile/', views.edit_profile, name= 'ProfileView'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/profile/', views.redirect_home, name='redirect_home'),
]
