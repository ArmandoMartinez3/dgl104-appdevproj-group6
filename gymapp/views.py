from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ExerciseForm, RoutineForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser, Exercise, Routine, RoutineExercise, TrainingSession
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,"home.html")

def about_us(request):
    return render(request, 'aboutus.html')

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
    # Get all clients
    clients = CustomUser.objects.filter(user_type='client')
    
    # Get training sessions for the current staff member
    training_sessions = TrainingSession.objects.filter(trainer=request.user)
    
    context = {
        'clients': clients,
        'training_sessions': training_sessions,
    }
    return render(request, 'staff/staff_home.html', context)

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
    # Allow both client and staff to view the routine
    if request.user.is_staff_member():
        routine = get_object_or_404(Routine, id=routine_id)
    else:
        routine = get_object_or_404(Routine, id=routine_id, user=request.user)
    
    exercises = RoutineExercise.objects.filter(routine=routine)
    context = {
        'routine': routine,
        'exercises': exercises,
        'is_staff': request.user.is_staff_member(),
    }
    return render(request, 'client/routine_detail.html', context)

@login_required
def toggle_exercise(request, routine_exercise_id):
    exercise = get_object_or_404(RoutineExercise, id=routine_exercise_id)
    exercise.completed = not exercise.completed
    exercise.completion_date = timezone.now() if exercise.completed else None
    exercise.save()
    return redirect('routine_detail', routine_id=exercise.routine.id)

@login_required
def add_exercise(request, routine_id):
    # Allow both client and staff to access the routine
    if request.user.is_staff_member():
        routine = get_object_or_404(Routine, id=routine_id)
    else:
        routine = get_object_or_404(Routine, id=routine_id, user=request.user)
    
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            RoutineExercise.objects.create(
                routine=routine,
                exercise=exercise
            )
            messages.success(request, 'Exercise added successfully.')
            return redirect('routine_detail', routine_id=routine.id)
    else:
        form = ExerciseForm()
    
    context = {
        'form': form,
        'routine': routine,
        'is_staff': request.user.is_staff_member(),
    }
    return render(request, 'client/add_exercise.html', context)

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

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def create_training_session(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        date = request.POST.get('date')
        time = request.POST.get('time')
        session_type = request.POST.get('session_type')
        
        try:
            client = CustomUser.objects.get(id=client_id, user_type='client')
            TrainingSession.objects.create(
                trainer=request.user,
                client=client,
                date=date,
                time=time,
                session_type=session_type
            )
            messages.success(request, 'Training session scheduled successfully.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid client selected.')
        except Exception as e:
            messages.error(request, f'Error scheduling session: {str(e)}')
    
    return redirect('staff_home')

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def edit_training_session(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id, trainer=request.user)
    
    if request.method == 'POST':
        session.date = request.POST.get('date')
        session.time = request.POST.get('time')
        session.session_type = request.POST.get('session_type')
        session.notes = request.POST.get('notes', '')
        session.save()
        messages.success(request, 'Session updated successfully.')
        return redirect('staff_home')
    
    return render(request, 'staff/edit_session.html', {'session': session})

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def cancel_training_session(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id, trainer=request.user)
    session.delete()
    messages.success(request, 'Session cancelled successfully.')
    return redirect('staff_home')

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def create_routine(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        name = request.POST.get('name')
        routine_type = request.POST.get('type')
        
        try:
            client = CustomUser.objects.get(id=client_id, user_type='client')
            routine = Routine.objects.create(
                user=client,
                name=name,
                routine_type=routine_type
            )
            messages.success(request, f'Routine "{name}" created successfully for {client.username}.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid client selected.')
        except Exception as e:
            messages.error(request, f'Error creating routine: {str(e)}')
    
    return redirect('staff_home')

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def client_details(request, client_id):
    client = get_object_or_404(CustomUser, id=client_id, user_type='client')
    routines = Routine.objects.filter(user=client)
    sessions = TrainingSession.objects.filter(client=client).order_by('date', 'time')
    
    context = {
        'client': client,
        'routines': routines,
        'sessions': sessions,
    }
    return render(request, 'staff/client_details.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def assign_routine_to_client(request, client_id):
    client = get_object_or_404(CustomUser, id=client_id, user_type='client')
    
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.user = client
            routine.save()
            messages.success(request, f'Routine "{routine.name}" assigned to {client.username}.')
            return redirect('client_details', client_id=client_id)
    else:
        form = RoutineForm()
    
    context = {
        'client': client,
        'form': form,
    }
    return render(request, 'staff/assign_routine.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def client_progress(request, client_id):
    client = get_object_or_404(CustomUser, id=client_id, user_type='client')
    routines = Routine.objects.filter(user=client)
    sessions = TrainingSession.objects.filter(client=client).order_by('-date', '-time')
    
    context = {
        'client': client,
        'routines': routines,
        'sessions': sessions,
    }
    return render(request, 'staff/client_progress.html', context)

@login_required
def delete_routines(request):
    if request.method == 'POST':
        routine_ids = request.POST.getlist('routine_ids')
        # Only delete routines that belong to the current user
        Routine.objects.filter(id__in=routine_ids, user=request.user).delete()
        messages.success(request, 'Selected routines have been deleted.')
    return redirect('client_home')

@login_required
@user_passes_test(lambda u: u.is_staff_member())
def edit_session(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    clients = CustomUser.objects.filter(is_staff=False)

    if request.method == 'POST':
        # Update session with new data
        session.date = request.POST.get('date')
        session.time = request.POST.get('time')
        session.client_id = request.POST.get('client')
        session.session_type = request.POST.get('session_type')
        session.save()
        
        messages.success(request, 'Training session updated successfully.')
        return redirect('staff_home')

    context = {
        'session': session,
        'clients': clients,
    }
    return render(request, 'staff/edit_session.html', context)
