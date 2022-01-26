from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"), #URL to home page
    path('signup/', views.SignupView.as_view(), name="signup"),
]

