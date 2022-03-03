from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Listing
from django.views.generic import FormView, ListView, DetailView, UpdateView
# Create your views here.


def home(response):
    return render(response, 'users/home.html', {})


class AddListing(FormView):
    pass

class DeleteListing():
    pass

class UpdateListing(FormView):
    pass

class DisplayListings(ListView):
    model = Listing
    context_object_name = "listing"
    template_name = "listings/display_listings.html"