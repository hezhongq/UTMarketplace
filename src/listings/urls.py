from urllib.parse import urlparse
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="listing-home"),  # URL to listing page
    path('add-listing/', views.AddListing.as_view(), name="add_listing"),  # URL to add listing page
<<<<<<< HEAD
    path('delete-listing/', views.DeleteListing.as_view(), name="delete_listing"),  # URL to delete listing page
    path('update-listing/', views.UpdateListing.as_view(), name="update_listing"),  # URL to update listing page
    path('display-listing/', views.DisplayListings.as_view(), name="display_listings"),  # URL to display listing page
=======
    path('delete-listing/', views.DeleteListing.as_view(), name="delete-listing"),  # URL to delete listing page
    path('update-listing/', views.UpdateListing.as_view(), name="update-listing"),  # URL to update listing page
    path('display-listing/', views.DisplayListings.as_view(), name="display-listings"),  # URL to display listing page
>>>>>>> a43984c ([UT-15] Updated urls to be able to access bookmarks page and added 'total cost' calculation)
]

