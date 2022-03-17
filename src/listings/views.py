from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from listings.models import Listing
from django.views.generic import FormView, ListView, DetailView, UpdateView
# Create your views here.

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
    
    def get_queryset(self):
        cost_from = self.request.GET.get('cost_from', 'give-default-value')
        cost_to = self.request.GET.get('cost_to', 'give-default-value')
        ctgry = self.request.GET.get('category', 'give-default-value')
        
        new_context = Listing.objects.filter(
            price__range=(cost_from, cost_to)
        ).filter(
            category=ctgry
        )
        return new_context
