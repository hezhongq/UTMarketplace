from urllib.parse import urlparse
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),  # URL to home page
    path('home/', views.home, name="home"),  # URL to home page
    path('signup/', views.register, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.do_logout, name="logout"),
    re_path(r'^active/(?P<active_code>.*)/$', views.active_user, name="active_user"),
    re_path(r'^reset/(?P<reset_code>.*)/$', views.forget_password_submit, name="reset_password"),
    path('forgetpassword/', views.reset_password, name="forgetpassword"),
    path('change_profile_password/', views.change_password, name="change_profile_password"),
    path('profile/', views.profile_view, name="view_profile"),
    path('edit_profile/', views.edit_avatar, name="edit_avatar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
