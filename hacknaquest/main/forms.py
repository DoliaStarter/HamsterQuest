from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(label="Name",
                           max_length=100)
    login = forms.CharField(label="Surname",
                            max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput)
