from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.conf import settings
from django.core.mail import send_mail

class HomeView(TemplateView):
    template_name='users/home.html'

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def send(request):
    subject = ''
    message = ''
    sender = settings.EMAIL_FROM
    receiver = []
    html_message = '<h1>TEST<h1>'
    send_mail(subject, message, sender, receiver, html_message=html_message)