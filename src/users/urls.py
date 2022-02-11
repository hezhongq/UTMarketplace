from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # URL to home page
    path('home/', views.home, name="home"),  # URL to home page
    path('signup/', views.register, name="signup"),
    path('login/', views.login, name="login"),
]

