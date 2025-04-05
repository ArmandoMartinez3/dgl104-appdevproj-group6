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
    path('about-us/', views.about_us, name='about_us'),
    path('client-home', views.client_home, name='client_home'),
    path('admin-home', views.admin_home, name='admin_home'),
    path('staff-home', views.staff_home, name='staff_home'),
    path('routine/add/', views.add_routine, name='add_routine'),
    path('routine/<int:routine_id>/', views.routine_detail, name='routine_detail'),
    path('exercise/toggle/<int:routine_exercise_id>/', views.toggle_exercise, name='toggle_exercise'),
    path('routine/<int:routine_id>/add-exercise/', views.add_exercise, name='add_exercise'),
    path('exercise/edit/<int:exercise_id>/', views.edit_exercise, name='edit_exercise'),
    path('exercise/delete/<int:exercise_id>/', views.delete_exercise, name='delete_exercise'),
    path('staff/create-routine/', views.create_routine, name='create_routine'),
    path('staff/create-session/', views.create_training_session, name='create_training_session'),
    path('staff/session/<int:session_id>/edit/', views.edit_session, name='edit_session'),
    path('staff/session/<int:session_id>/cancel/', views.cancel_training_session, name='cancel_training_session'),
    path('staff/client/<int:client_id>/', views.client_details, name='client_details'),
    path('staff/client/<int:client_id>/assign-routine/', views.assign_routine_to_client, name='assign_routine_to_client'),
    path('staff/client/<int:client_id>/progress/', views.client_progress, name='client_progress'),
    path('delete-routines/', views.delete_routines, name='delete_routines'),
]