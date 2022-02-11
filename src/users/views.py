from .forms import LoginForm, RegistrationForm
from .models import UserExtension
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import auth


def home(response):
    return render(response, 'users/home.html', {})


def register(response):
    error = []
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password != password2:
                return HttpResponse("two passwords do not match with each other")
            if not UserExtension.objects.all().filter(email=email):
                user = UserExtension()
                user.username = username
                user.email = email
                user.set_password(password2)
                user.save()
                return HttpResponse("success")
            else:
                return HttpResponse("user exists")
    else:
        form = RegistrationForm()

    return render(response, "users/signup.html", {'form': form, 'error': error})


def login(response):
    if response.method == 'POST':
        form = LoginForm(response.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(response, user)
                return render(response, 'users/home.html', {})
            else:
                return HttpResponse("wrong user email or password")
    else:
        form = LoginForm()

    return render(response, "users/login.html", {'form': form})


def do_logout(response):
    auth.logout(response)
    return HttpResponseRedirect('/')


def send(request):
    subject = ''
    message = ''
    sender = settings.EMAIL_FROM
    receiver = []
    html_message = '<h1>TEST<h1>'
    send_mail(subject, message, sender, receiver, html_message=html_message)
