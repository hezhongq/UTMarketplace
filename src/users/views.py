from .forms import RegistrationForm, LoginForm
from .models import UserExtension
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(response):
    return render(response, 'users/users/home.html', {})

def register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']

            user = User.objects.create_user(username=username, password=password)
            user_extension = UserExtension(user)
            user_extension.save()

        return HttpResponseRedirect("")
    else:
        form = RegistrationForm()
    
    return render(response, "users/signup.html", {'form': form})

def login(response):
    if response.method == 'POST':
        form = LoginForm(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(response, user)
                return HttpResponseRedirect(reverse('users:profile', args=[user.id]))
            else:
                return render(response, 'users/login.html', {'form': form, 'message': 'wrong password'})
    else:
        form = LoginForm()
    
    return render(response, "users/login.html", {'form': form})

def send(request):
    subject = ''
    message = ''
    sender = settings.EMAIL_FROM
    receiver = []
    html_message = '<h1>TEST<h1>'
    send_mail(subject, message, sender, receiver, html_message=html_message)