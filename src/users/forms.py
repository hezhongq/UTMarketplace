from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(label='email')
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput())

    def clean(self):
        email_data = self.cleaned_data['email']
        if "@mail.utoronto.ca" not in email_data:
            raise forms.ValidationError("Must be a utoronto address")
        if not self.is_valid():
            raise forms.ValidationError('Please input all fields in form')
        elif self.cleaned_data['password2'] != self.cleaned_data['password']:
            raise forms.ValidationError('2 passwords do not match with each other')
        else:
            cleaned_data = super(RegisterForm, self).clean()
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('Please input all fields in form')
        cleaned_data = super(LoginForm, self).clean()
        return cleaned_data
