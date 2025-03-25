from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_admin():
                return redirect('admin_home')
            elif user.is_staff_member():
                return redirect('staff_home')
            else:
                return redirect('client_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_admin())
def admin_home(request):
    users = CustomUser.objects.all().order_by('username')
    return render(request, 'admin/admin_home.html', {'users': users})

@login_required
@user_passes_test(lambda u: u.is_admin())
def update_user_role(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=user_id)
        user.user_type = request.POST.get('user_type')
        user.save()
        messages.success(request, f'Role updated for {user.username}')
    return redirect('admin_home')

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def staff_home(request):
    return render(request, 'staff/staff_home.html')

@login_required
@user_passes_test(lambda u: u.is_client())
def client_home(request):
    return render(request, 'client/client_home.html')
