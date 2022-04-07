from urllib.parse import urlparse
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),                                          # URL to home end point
    path('home/', views.home, name="home"),                                     # URL to home end point
    path('signup/', views.register, name="signup"),                             # URL to signup end point
    path('login/', views.login, name="login"),                                  # URL to login end point
    path('logout/', views.do_logout, name="logout"),                            # URL to logout end point
    path('search_results/', views.search_results,                               # URL to search_results end point
          name="search_results"),

    path('edit_profile/', views.edit_profile, name="edit_profile"),             # URL to edit_profile end point
    path('bookmarks/', views.BookmarksView.as_view(),                           # URL to view_bookmarks end point
          name="view_bookmarks"),

    path('bookmarks/<int:pk>/delete',                                           # URL to delete_bookmark end point
          views.DeleteBookmark.as_view(), name="delete_bookmark"),

    re_path(r'^active/(?P<active_code>.*)/$',                                   # URL to active_user end point
            views.active_user, name="active_user"),

    re_path(r'^reset/(?P<reset_code>.*)/$',                                     # URL to reset_password end point
            views.forget_password_submit, name="reset_password"),

    path('forgetpassword/', views.reset_password, name="forgetpassword"),       # URL to forgetpassword end point
    path('change_profile_password/', views.change_password,                     # URL to change_profile_password end point
          name="change_profile_password"),

    path('rate/', views.add_rate, name="add_rate"),                             # URL to add_rate end point
    path('profile/<int:user_id>', views.profile, name="profile"),               # URL to profile end point
    path('report/<int:user_id>', views.report, name="report"),                  # URL to report end point
    path('delete_account/<int:user_id>',                                        # URL to delete_account end point
          views.delete_account, name="delete_account"),

    re_path(r'^delete_account_confirm/(?P<delete_account_confirm_code>.*)/$',   # URL to delete_account_confirm end point
            views.delete_account_confirm, name="delete_account_confirm"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
