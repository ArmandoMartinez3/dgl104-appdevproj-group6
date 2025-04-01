from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Exercise, Routine, RoutineExercise

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'address', 'password1', 'password2')

class ExerciseForm(forms.ModelForm):
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

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        } 