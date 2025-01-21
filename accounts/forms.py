from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import customuser
from django.contrib.auth.forms import AuthenticationForm


class registrationform(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = customuser
        fields = ['username', 'email', 'birth_date', 'password1', 'password2']

class customloginform(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']