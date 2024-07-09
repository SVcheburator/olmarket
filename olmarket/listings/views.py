from django.shortcuts import render, redirect
from .models import Listing, ListingImage
from .forms import ListingForm, ListingImageForm


def create_listing(request):
    if request.method == 'POST':
        listing_form = ListingForm(request.POST)
        image_form = ListingImageForm(request.POST, request.FILES)
        
        files = request.FILES.getlist('image')
        
        if listing_form.is_valid():
            listing = listing_form.save(commit=False)
            listing.user = request.user
            listing.save()

            for file in files:
                ListingImage.objects.create(listing=listing, image=file)
            
            return redirect(to='main:main')
        else:
            print(listing_form.errors)
    else:
        listing_form = ListingForm()
        image_form = ListingImageForm()

    return render(request, 'listings/create_listing.html', {
        'listing_form': listing_form,
        'image_form': image_form,
    })
