from urllib.parse import urlparse
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.DisplayListings.as_view(), name="listing-home"),  # URL to listing page
    path('add-listing/', views.AddListing.as_view(), name="add_listing"),  # URL to add listing page
    path('delete-listing/', views.DeleteListing.as_view(), name="delete-listing"),  # URL to delete listing page
    path('update-listing/', views.UpdateListing.as_view(), name="update-listing"),  # URL to update listing page
    path('display-listing/', views.DisplayListings.as_view(), name="display-listings"),  # URL to display listing page
    path('listings/<int:pk>/details/', views.SingleListing.as_view(), name="single-listing"),  # URL to display listing page

]

