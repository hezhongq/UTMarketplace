from .forms import LoginForm, RegistrationForm, ResetPasswordForm, EditUserForm
from .models import UserExtension
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import auth
from random import Random
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from .models import EmailVerifyRecord
from django.views.generic import ListView, DeleteView
from listings.models import Listing, Bookmark


def home(response):
    if response.user.is_authenticated:
        return render(response, 'users/home.html', {})
    else:
        return redirect('/users/login/')


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
                send_email(response.get_host(), email, "register")
                return redirect('/users/login/')
            else:
                error = "user exists\n"
                return render(response, "users/signup.html", {'form': form, 'error': error})
    else:
        form = RegistrationForm()
    return render(response, "users/signup.html", {'form': form, 'error': error})


def login(response):
    error = ""
    if response.user.is_authenticated:
        return redirect('/')
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
                send_email(response.get_host(), email, "forget")
                return render(response, "users/result.html", {'success': "email sent"})
            return render(response, "users/result.html", {'error': "no this user"})
    else:
        form = ResetPasswordForm()
    return render(response, "users/pwd_retrieval.html", {'form': form, 'error': error})


def change_password(response):
    if not response.user.is_authenticated:
        return render(response, "users/result.html", {'error': "please login"})
    if response.method == "POST":
        form = PasswordChangeForm(user=response.user, data=response.POST)
        if form.is_valid():
            user = form.save()
            auth.update_session_auth_hash(response, user)
            return redirect('/users/profile/{0}'.format(user.id))
    else:
        form = PasswordChangeForm(user=response.user)
    return render(response, "users/change_profile_password.html", {'form': form})


def search_results(request):
    if request.method == 'POST':
        searched = request.POST['search']
        listings = Listing.objects.filter(item_name__contains=searched)
        paginator = Paginator(listings, 10)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # return render(request, "users/search_results.html", {'searched': searched, 'listings': listings})
        return render(request, "users/search_results.html", {'page_obj': page_obj, 'searched': searched})

    else:
        return render(request, "users/search_results.html", {})


def profile(response, user_id):
    user = UserExtension.objects.filter(id=user_id)
    if user_id == response.user.id:            
        return render(response, "users/profile.html", {'user': user[0], 'listing_set': user[0].listing_set.all(), 'is_user': True,
                                                       'star_range': range(int(user[0].rate)),
                                                       'half_star': (user[0].rate - int(user[0].rate) >= 0.5),
                                                       'star_empty': range(int(5 - user[0].rate))
                                                       })
    elif user:
        return render(response, "users/profile.html", {'user': user[0], 'listing_set': user[0].listing_set.all(), 'is_user': False,
                                                       'star_range': range(int(user[0].rate)),
                                                       'half_star': (user[0].rate - int(user[0].rate) >= 0.5),
                                                       'star_empty': range(int(5 - user[0].rate))})
    else:
        return render(response, "users/result.html", {'error': "no this user"})



def edit_profile(response):
    user = response.user
    form = EditUserForm()
    if not user.is_authenticated:
        return redirect(reverse('login'))
    if response.method == "POST":
        form = EditUserForm(response.POST)
        if form.is_valid():
            if len(form.cleaned_data['username']) > 0:
                user.username = form.cleaned_data['username']
            if 'avatar' in response.FILES:
                user.avatar = response.FILES['avatar']
            user.save()
            return redirect(reverse('profile', kwargs={'user_id': user.id}))
    return render(response, "users/edit_profile.html", {'user': user, 'form': form, 'is_user': True})


def delete_account(response, user_id):
    user = UserExtension.objects.filter(id=user_id)
    if user_id == response.user.id:
        email = response.user.email
        send_email(response.get_host(), email, "delete")
        return redirect('/users/login/')
    elif user:
        return render(response, "users/result.html", {"error": "access denied"})
    else:
        return render(response, "users/result.html", {"error": "no account exists"})


def delete_account_confirm(response, delete_account_confirm_code):
    all_records = EmailVerifyRecord.objects.filter(code=delete_account_confirm_code, send_type="delete")
    if all_records:
        for record in all_records:
            email = record.email
            user = UserExtension.objects.all().filter(email=email)
            if user:
                user[0].is_active = True
                user[0].delete()
                return render(response, "users/result.html", {'success': "account deleted"})
            return render(response, "users/result.html", {'error': "user does not exist"})
    return render(response, "users/result.html", {'error': "code does not exist"})


class DeleteBookmark(DeleteView):
    model = Bookmark
    context_object_name = 'bookmark'
    success_url = "/users/bookmarks"

    def get(self, request, *args, **kwargs):
        print(self.kwargs['pk'])
        bookmark = Bookmark.objects.get(id=self.kwargs['pk'])
        bookmark.delete()
        return redirect("/users/bookmarks")

'''===helpers==='''

def random_str(randomlength=8):
    s = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        s += chars[random.randint(0, length)]
    return s


def send_email(hostname, email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code + email
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "UTMarketplace - register code"
        email_body = "click to verify: http://{0}/users/active/{1}".format(hostname, code + email)

    elif send_type == "forget":
        email_title = "UTMarketplace - Password Reset"
        email_body = "Click here to reset password: http://{0}/users/reset/{1}".format(hostname, code + email)

    elif send_type == "delete":
        email_title = "UTMarketplace - Delete Account"
        email_body = "Click here to confirm account deletion: http://{0}/users/delete_account_confirm/{1}".format(hostname, code + email)

    send_status = send_mail(email_title, email_body, settings.EMAIL_HOST_USER, [email])
    if not send_status:
        print("send email failed")


# Bookmark listing view
class BookmarksView(ListView):
    model = Bookmark
    context_object_name = "bookmarks"
    template_name = 'users/bookmarks.html'

    # We get the total price of all items in the user's bookmarks
    def get_context_data(self, **kwargs):
        cost = 0
        for bookmark in Bookmark.objects.filter(owner=self.request.user):
            cost += bookmark.listing.price
        context = super().get_context_data(**kwargs)
        context['total_cost'] = cost
        return context

    # Make the queryset return all bookmarks that belong to the user
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
