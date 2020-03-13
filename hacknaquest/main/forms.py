from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    action = "Register"
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username',  'password')


class SignInForm(forms.Form):
    action = "Sign in"
    username = forms.CharField(label="Login",
                            max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SessionManagerMainForm(forms.Form):    
    photo = forms.ImageField(label='') #widget=forms.ImageField(attrs={'id': 'photo'}))
    answer = forms.CharField(label='', max_length=100,
                        widget=forms.TextInput(attrs={'id': 'answer', 'placeholder': 'Answer...'}))
