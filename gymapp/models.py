from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Administrator'),
        ('staff', 'Staff'),
        ('client', 'Client')
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='client')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    class Meta:
        db_table = 'gymapp_customuser'

    def is_admin(self):
        return self.user_type == 'admin' or self.is_superuser
    
    def is_staff_member(self):
        return self.user_type == 'staff'
    
    def is_client(self):
        return self.user_type == 'client'

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Routine(models.Model):
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
    
    def __str__(self):
        return f"{self.user.username}'s {self.name}"

class RoutineExercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['id']

class TrainingSession(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date', 'time']
    
    def __str__(self):
        return f"{self.client.username} - {self.date} {self.time}"
