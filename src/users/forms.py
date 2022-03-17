from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserExtension


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = UserExtension
        fields = ("username", "email",)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def clean_email(self):
        email_data = self.cleaned_data.get('email')
        if "@mail.utoronto.ca" not in email_data:
            raise forms.ValidationError("Must be a utoronto address")
        return email_data




# Will not use this form
'''
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
'''


class LoginForm(forms.Form):
    email = forms.EmailField(label='email', required=True, min_length=1,
                             widget=forms.TextInput({'placeholder': 'Email'}))
    password = forms.CharField(label='password', required=True, min_length=8,
                               widget=forms.PasswordInput({'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('Please input all fields in form')
        cleaned_data = super(LoginForm, self).clean()
        return cleaned_data


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label='email', required=True, min_length=1,
                             widget=forms.TextInput({'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('Please input all fields in form')
        cleaned_data = super(ResetPasswordForm, self).clean()
        return cleaned_data


class EditUserForm(forms.Form):
    username = forms.CharField(required=False, max_length=20)
    avatar = forms.ImageField(required=False)
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = UserExtension
        fields = ("username", "avatar")
