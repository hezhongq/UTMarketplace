from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse

from listings.forms.add_listing import AddListingForm
from users.models import Category

from .models import Listing
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView, DeleteView
# Create your views here.


def home(response):
    return render(response, 'users/display_listings.html', {})


class AddListing(FormView):
    template_name = 'listings/add_listing.html'
    form_class = AddListingForm

    def form_valid(self, form):
        # Create the new listing here after validating data. Redirect to success URL if listing was successfully created
        
        category_name = form.cleaned_data.pop('category')
        print(category_name) 
        category_object = Category.objects.get(name=category_name)
        

        # Might need to change original_poster to abstract user by doing a query
        Listing.objects.create(**form.cleaned_data, category=category_object, original_poster=self.request.user)
        return redirect("/listings")

# Ensure that only the user who created this post can delete it
class DeleteListing(DeleteView):
    model = Listing
    context_object_name = 'listing'
    template_name = 'listings/delete_listing.html'

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

class SingleListing(DetailView):
    model = Listing
    context_object_name = "listing"
    template_name = "listings/single_listing.html"
    
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
