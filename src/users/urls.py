from urllib.parse import urlparse
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # URL to home page
    path('home/', views.home, name="home"),  # URL to home page
    path('signup/', views.register, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.do_logout, name="logout"),
    path('search_results/', views.search_results, name="search_results"),
    re_path(r'^active/(?P<active_code>.*)/$', views.active_user, name="active_user")
]

