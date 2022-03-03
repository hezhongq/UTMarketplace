from urllib.parse import urlparse
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # URL to home page
    path('listings/', views.home, name="home"),  # URL to listing page
    path('add-listing/', views.AddListing, name="add_listing"),  # URL to add listing page
    path('delete-listing/', views.DeleteListing, name="delete-listing"),  # URL to delete listing page
    path('update-listing/', views.UpdateListing, name="update-listing"),  # URL to update listing page
    path('display-listing/', views.DisplayListings, name="display-listings"),  # URL to display listing page
]

