# Gym Project Documentation

## Overview

This project is a comprehensive gym management system built with Django. It provides features for managing gym members, staff, clients, routines, exercises, and training sessions.

## System Architecture

### Core Components

1. **Main Application (`gymapp/`)**
   - User management (Admin, Staff, Clients)
   - Exercise and routine management
   - Training session scheduling
   - Progress tracking

2. **Project Configuration (`User_Gymproject/`)**
   - Django settings
   - URL routing
   - Middleware configuration
   - Database settings

### Database Structure

The project uses SQLite for development. Key database tables include:

- CustomUser (extends AbstractUser)
- Exercise
- Routine
- RoutineExercise
- TrainingSession

## Technical Implementation Details

### Django Models

#### CustomUser Model
```python
class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Implements different user types: admin, staff, and client.
    """
    USER_TYPES = (
        ('admin', 'Administrator'),
        ('staff', 'Staff'),
        ('client', 'Client')
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='client')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def is_admin(self):
        return self.user_type == 'admin' or self.is_superuser
    
    def is_staff_member(self):
        return self.user_type == 'staff'
    
    def is_client(self):
        return self.user_type == 'client'
```

#### Exercise Model
```python
class Exercise(models.Model):
    """
    Represents a gym exercise with its specifications.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
```

#### Routine Model
```python
class Routine(models.Model):
    """
    Represents a workout routine assigned to a user.
    """
    ROUTINE_TYPES = (
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
        ('hiit', 'HIIT')
    )
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    routine_type = models.CharField(max_length=20, choices=ROUTINE_TYPES, default='strength')
    date_created = models.DateTimeField(auto_now_add=True)
```

#### TrainingSession Model
```python
class TrainingSession(models.Model):
    """
    Represents a scheduled training session between a trainer and client.
    """
    SESSION_TYPES = (
        ('personal', 'Personal Training'),
        ('group', 'Group Training'),
        ('assessment', 'Assessment')
    )
    
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='training_sessions')
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='client_sessions')
    date = models.DateField()
    time = models.TimeField()
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES)
    notes = models.TextField(blank=True)
```

### Django Views

#### Authentication Views
```python
class CustomLoginView(LoginView):
    """
    Custom login view that redirects users based on their type.
    """
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
```

#### Staff Views
```python
@login_required
@user_passes_test(lambda u: u.is_staff_member())
def staff_home(request):
    """
    Staff dashboard showing clients and training sessions.
    """
    clients = CustomUser.objects.filter(user_type='client')
    training_sessions = TrainingSession.objects.filter(trainer=request.user)
    
    context = {
        'clients': clients,
        'training_sessions': training_sessions,
    }
    return render(request, 'staff/staff_home.html', context)
```

#### Client Views
```python
@login_required
@user_passes_test(lambda u: u.is_client())
def client_home(request):
    """
    Client dashboard showing their routines.
    """
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'client/client_home.html', {'routines': routines})
```

### Django Forms

#### User Registration
```python
class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form with additional fields.
    """
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'address', 'password1', 'password2')
```

#### Exercise Form
```python
class ExerciseForm(forms.ModelForm):
    """
    Form for creating and editing exercises.
    """
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'sets', 'reps', 'weight']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'rows': 3}),
            'sets': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'reps': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        }
```

## Security Implementation

### Authentication
- Custom user model extending AbstractUser
- Role-based access control (admin, staff, client)
- Login required decorators for protected views
- User type specific permissions

### Authorization
- Staff members can only access staff-specific views
- Clients can only access their own data
- Admins have full access to all features

## User Roles and Permissions

### Administrator
- Full system access
- User management
- Staff management
- System configuration

### Staff Member
- Client management
- Training session scheduling
- Routine creation and assignment
- Progress tracking

### Client
- View assigned routines
- Track exercise progress
- View training sessions
- Update personal information

## Development Workflow

### Setting Up Development Environment

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies from requirements.txt
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Start development server: `python manage.py runserver`

### Code Style Guidelines

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Write unit tests for new features

## Deployment

### Production Setup

1. Configure production settings
2. Set up PostgreSQL database
3. Configure environment variables
4. Set up Gunicorn
5. Configure static files
6. Set up SSL certificate

### Environment Variables

Required environment variables:
- `SECRET_KEY`
- `DEBUG`
- `DATABASE_URL`
- `ALLOWED_HOSTS`
- `EMAIL_HOST`
- `EMAIL_PORT`

## Support and Contact

For technical support or questions:
- Email: [Support Email]
- Documentation: [Documentation URL]
- Issue Tracker: [Issue Tracker URL]
