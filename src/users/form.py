from cProfile import label
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 50:
            raise forms.ValidationError("Please wirte the proper email")
        else:
            filter_result = User.objects.filter(username__exact = username)
            if filter_result.exists():
                raise forms.ValidationError("Your username exists")
        
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError("Your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long")
        
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Confirm Password is not matching")
        
        return password2
