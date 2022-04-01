from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

from listings.forms.add_listing import AddListingForm, EditListingForm

from listings.models import Listing, Bookmark, Category
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
        print('============')
        print(category_name) 
        category_object = Category.objects.get(name=category_name)
        
        print('============')
        print(form.cleaned_data) 
        # Might need to change original_poster to abstract user by doing a query
        new_listing = Listing.objects.create(**form.cleaned_data, category=category_object, original_poster=self.request.user)
        print(f"/listings/{new_listing.id}/details/")
        return redirect(f"/listings/{new_listing.id}/details/")



# Ensure that only the user who created this post can delete it
class DeleteListing(DeleteView):
    model = Listing
    context_object_name = 'listing'
    template_name = 'listings/delete_listing.html'


class UpdateListing(UpdateView):
    model = Listing
    context_object_name = 'listing'
    template_name = 'listings/edit_listing.html'
    fields = [
        "image"
    ]

    # Specify the success url here
    def get_success_url(self):
       pass 

    def form_valid(self, form):
        print("=++++===+==+++=+=")
        self.object.groups.clear()
        self.object.groups.add(form.cleaned_data['image'])
        return super().form_valid(form)

class DisplayListings(ListView):
    model = Listing
    context_object_name = "listings"
    template_name = "listings/display_listings.html"

    def get_queryset(self):
        cost_from = self.request.GET.get('start-price', -1)
        cost_to = self.request.GET.get('end-price', -1)
        # if nothing in text boxes, return Listings.objects.all()
        if cost_from == -1 and cost_to == -1:
            return Listing.objects.all()

        # if thing in text boxes, parse it and return filtered version
        
        # ctgry = self.request.GET.get('category', 'give-default-value')
        
        new_context = Listing.objects.filter(
            price__range=(cost_from, cost_to)
        )#  .filter(category=ctgry)
        return new_context

class SingleListing(DetailView):
    model = Listing
    context_object_name = "listing"
    template_name = "listings/single_listing.html"

def bookmark_listing(request, pk):
    given_listing = get_object_or_404(Listing, id=pk)
    existing_bookmarks = Bookmark.objects.filter(owner=request.user)

    for bookmark in existing_bookmarks:
        # The user has already bookmarked this listing
        if bookmark.listing == given_listing and bookmark.owner == request.user:
            Bookmark.objects.get(id=bookmark.id).delete()

            if request.POST['url_type'] == 'all_listings':
                return redirect('/listings/')
            return redirect(f'/listings/{pk}/details/')

    new_bookmark = Bookmark(owner=request.user, listing=given_listing)
    new_bookmark.save()
    if request.POST['url_type'] == 'all_listings':
        return redirect('/listings/')
    return redirect(f'/listings/{pk}/details/')


def edit_listing_img(request, pk):

    user = request.user
    form = EditListingForm()
    listing = Listing.objects.filter(id=pk)
    if not user.is_authenticated:
        return redirect(reverse('login'))
    if request.method == "POST":
        form = EditListingForm(request.POST)
        if form.is_valid():
            if 'image' in request.FILES:
                user.avatar = request.FILES['image']
            user.save()
            print("===============")
            return redirect(reverse('profile', kwargs={'user_id': user.id}))
    return render(request, "listings/edit_listing.html", {'user': user, 'listing': listing, 'form': form, 'is_user': True})