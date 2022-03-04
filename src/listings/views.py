from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse

from listings.forms.add_listing import AddListingForm

from .models import Listing
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView, DeleteView
# Create your views here.


def home(response):
    return render(response, 'users/home.html', {})


class AddListing(FormView):
    template_name = 'listings/add_listing.html'
    form_class = AddListingForm

    def form_valid(self, form):
        # Create the new listing here after validating data. Redirect to success URL if listing was successfully created
        pass

# Ensure that only the user who created this post can delete it
class DeleteListing(DeleteView):
    model = Listing

    def get_object(self):
        # Look for the object that belongs to the user here
        pass

    def get_success_url(self):
        pass

class UpdateListing(UpdateView):
    model = Listing
    context_object_name = 'listing'
    template_name = 'listings/edit_listing.html'

    # Specify the success url here
    def get_success_url(self):
       pass 

class DisplayListings(ListView):
    model = Listing
    context_object_name = "listing"
    template_name = "listings/display_listings.html"