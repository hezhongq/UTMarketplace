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
    path('search_results/', views.search_results, name="search_results"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('bookmarks/', views.BookmarksView.as_view(), name="view_bookmarks"),
    path('bookmarks/<int:pk>/delete', views.DeleteBookmark.as_view(), name="delete_bookmark"),
    re_path(r'^active/(?P<active_code>.*)/$', views.active_user, name="active_user"),
    re_path(r'^reset/(?P<reset_code>.*)/$', views.forget_password_submit, name="reset_password"),
    path('forgetpassword/', views.reset_password, name="forgetpassword"),
    path('change_profile_password/', views.change_password, name="change_profile_password"),
    path('profile/<int:user_id>', views.profile, name="profile"),
    path('report/<int:user_id>', views.report, name="report"),
    path('delete_account/<int:user_id>', views.delete_account, name="delete_account"),
    re_path(r'^delete_account_confirm/(?P<delete_account_confirm_code>.*)/$', views.delete_account_confirm, name="delete_account_confirm"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
