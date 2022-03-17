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
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('bookmarks/', views.BookmarksView.as_view(), name="bookmarks"),
    re_path(r'^active/(?P<active_code>.*)/$', views.active_user, name="active_user"),
    re_path(r'^reset/(?P<reset_code>.*)/$', views.forget_password_submit, name="reset_password"),
    path('forgetpassword/', views.reset_password, name="forgetpassword"),
    path('change_profile_password/', views.change_password, name="change_profile_password"),
    path('profile/<int:user_id>', views.profile, name="profile"),
]

