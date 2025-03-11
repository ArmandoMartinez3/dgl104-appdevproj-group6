from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'), 
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(next_page='signin'), name='signout'),
]