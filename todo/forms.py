from django import forms
from .models import ToDoItem,Reminder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pssword2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class TaskForm(forms.ModelForm):
    class Meta:
        model=ToDoItem
        fields=["title"]


# forms.py



class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['time','todo_item']
