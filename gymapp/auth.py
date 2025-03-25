from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_admin():
                return '/admin-home'
            elif user.is_staff_member():
                return '/staff-home'
            else:
                return '/client-home'
        return '/' 