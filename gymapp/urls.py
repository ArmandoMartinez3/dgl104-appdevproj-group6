from django.urls import path
from . import views
from .auth import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'), 
    path('signup/', views.signup, name='signup'),
    path('signin/', CustomLoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(next_page='signin'), name='signout'),
    path('update-user-role/<int:user_id>/', views.update_user_role, name='update_user_role'),
    path('client-home', views.client_home, name='client_home'),
    path('admin-home', views.admin_home, name='admin_home'),
    path('staff-home', views.staff_home, name='staff_home'),
]