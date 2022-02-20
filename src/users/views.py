from .forms import LoginForm, RegistrationForm
from .models import UserExtension
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import auth


def home(response):
    return render(response, 'users/home.html', {})


def register(response):
    error = ""
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password != password2:
                error = "two passwords do not match with each other\n"
                return render(response, "users/signup.html", {'form': form, 'error': error})
            if not UserExtension.objects.all().filter(email=email):
                user = UserExtension()
                user.username = username
                user.email = email
                user.set_password(password2)
                user.save()
                return HttpResponse("success")
            else:
                error = "user exists\n"
                return render(response, "users/signup.html", {'form': form, 'error': error})
    else:
        form = RegistrationForm()
    return render(response, "users/signup.html", {'form': form, 'error': error})


def login(response):
    error = ""
    if response.method == 'POST':
        form = LoginForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(response, user)
                return redirect('/users/home/')
            else:
               error = "wrong user email or password\n"
    else:
        form = LoginForm()

    return render(response, "users/login.html", {'form': form, 'error': error})


def do_logout(response):
    auth.logout(response)
    return HttpResponseRedirect('/users/login')


def send(request):
    subject = ''
    message = ''
    sender = settings.EMAIL_FROM
    receiver = []
    html_message = '<h1>TEST<h1>'
    send_mail(subject, message, sender, receiver, html_message=html_message)
