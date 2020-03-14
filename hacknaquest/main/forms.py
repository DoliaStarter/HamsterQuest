from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    action = "Register"
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username',  'password')


class SignInForm(forms.Form):
    action = "Sign in"
    login = forms.CharField(label="Login",
                            max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

