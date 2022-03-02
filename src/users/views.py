from .forms import LoginForm, RegistrationForm, ResetPasswordForm
from .models import UserExtension
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from random import Random
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from .models import EmailVerifyRecord


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
                send_register_email(response.get_host(), email, "register")
                return redirect('/users/login/')
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
                if not user.is_active:
                    error = "user not active\n"
                    return render(response, "users/login.html", {'form': form, 'error': error})
                auth.login(response, user)
                return redirect('/users/home/')
            else:
                error = "wrong user email or password\n"
    else:
        form = LoginForm()

    return render(response, "users/login.html", {'form': form, 'error': error})


def do_logout(response):
    auth.logout(response)
    return redirect('/users/login')


def active_user(response, active_code):
    all_records = EmailVerifyRecord.objects.filter(code=active_code, send_type="register")
    if all_records:
        # should we avoid same record?
        for record in all_records:
            email = record.email
            user = UserExtension.objects.all().filter(email=email)
            if user:
                user[0].is_active = True
                user[0].save()
                return render(response, "users/result.html", {'success': "verify account successfully"})
            return render(response, "users/result.html", {'error': "no this user"})
    return render(response, "users/result.html", {'error': "no this code"})


def forget_password_submit(response, reset_code):
    all_records = EmailVerifyRecord.objects.filter(code=reset_code, send_type="forget")
    if all_records:
        # should we avoid same record?
        for record in all_records:
            email = record.email
            user = UserExtension.objects.all().filter(email=email)
            if user:
                user = UserExtension.objects.get(email=email)
                if response.method == 'POST':
                    form = SetPasswordForm(user=user, data=response.POST)
                    if form.is_valid():
                        form.save()
                        return render(response, "users/result.html",
                                      {'success': "reset password successfully"})
                    else:
                        return render(response, "users/reset.html",
                                      {'form': form})
                else:
                    form = SetPasswordForm(user=user)
                    return render(response, "users/reset.html",
                                  {'form': form})
            else:
                return render(response, "users/result.html",
                              {'error': "no this user"})
    return render(response, "users/result.html",
                  {'error': "no this code"})

def reset_password(response):
    error = ""
    if response.method == 'POST':
        form = ResetPasswordForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = UserExtension.objects.all().filter(email=email)
            if user:
               send_register_email(response.get_host(), email, "forget")
               return render(response, "users/result.html", {'success': "email sent"})
                
            return render(response, "users/result.html", {'error': "no this user"})


    else:
        form = ResetPasswordForm()

    return render(response, "users/pwd_retrieval.html", {'form': form, 'error': error})


'''===helpers==='''


def random_str(randomlength=8):
    s = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        s += chars[random.randint(0, length)]
    return s


def send_register_email(hostname, email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code + email
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "UTMarketplace - register code"
        email_body = "click to verify: http://{0}/users/active/{1}".format(hostname, code)

    elif send_type == "forget":
        email_title = "UTMarketplace - Password Reset"
        email_body = "Click here to reset password: http://{0}/users/reset/{1}".format(hostname, code)

    send_status = send_mail(email_title, email_body, settings.EMAIL_HOST_USER, [email])
    if not send_status:
        print("send email failed")
