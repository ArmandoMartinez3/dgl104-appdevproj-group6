from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ExerciseForm, RoutineForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser, Exercise, Routine, RoutineExercise
from django.contrib import messages
from django.utils import timezone

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
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'client/client_home.html', {'routines': routines})

@login_required
def add_routine(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.user = request.user
            routine.save()
            return redirect('routine_detail', routine_id=routine.id)
    else:
        form = RoutineForm()
    return render(request, 'client/add_routine.html', {'form': form})

@login_required
def routine_detail(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id, user=request.user)
    exercises = RoutineExercise.objects.filter(routine=routine)
    return render(request, 'client/routine_detail.html', {
        'routine': routine,
        'exercises': exercises
    })

@login_required
def toggle_exercise(request, routine_exercise_id):
    exercise = get_object_or_404(RoutineExercise, id=routine_exercise_id)
    exercise.completed = not exercise.completed
    exercise.completion_date = timezone.now() if exercise.completed else None
    exercise.save()
    return redirect('routine_detail', routine_id=exercise.routine.id)

@login_required
def add_exercise(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id, user=request.user)
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            RoutineExercise.objects.create(
                routine=routine,
                exercise=exercise
            )
            return redirect('routine_detail', routine_id=routine.id)
    else:
        form = ExerciseForm()
    return render(request, 'client/add_exercise.html', {
        'form': form,
        'routine': routine
    })

@login_required
def edit_exercise(request, exercise_id):
    routine_exercise = get_object_or_404(RoutineExercise, id=exercise_id)
    exercise = routine_exercise.exercise
    
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('routine_detail', routine_id=routine_exercise.routine.id)
    else:
        form = ExerciseForm(instance=exercise)
    
    return render(request, 'client/edit_exercise.html', {
        'form': form,
        'routine_exercise': routine_exercise
    })

@login_required
def delete_exercise(request, exercise_id):
    routine_exercise = get_object_or_404(RoutineExercise, id=exercise_id)
    routine_id = routine_exercise.routine.id
    routine_exercise.delete()
    return redirect('routine_detail', routine_id=routine_id)
