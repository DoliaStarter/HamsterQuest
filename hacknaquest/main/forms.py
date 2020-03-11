from django import forms


class RegistrationForm(forms.Form):
    action = "Register"
    name = forms.CharField(label="Name",
                           max_length=100)
    login = forms.CharField(label="Login",
                            max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput)


class SignInForm(forms.Form):
    action = "Sign in"
    login = forms.CharField(label="Login",
                            max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput)


class SessionManagerMainForm(forms.Form):    
    photo = forms.ImageField(label='') #widget=forms.ImageField(attrs={'id': 'photo'}))
    answer = forms.CharField(label='', max_length=100,
                        widget=forms.TextInput(attrs={'id': 'answer', 'placeholder': 'Answer...'}))
