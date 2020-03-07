from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(label="Your name",
                           max_length=100)
