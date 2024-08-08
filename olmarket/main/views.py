from django.shortcuts import render

from listings.models import Listing

# Create your views here.
def main(request):
    listings = Listing.objects.all()

    for listing in listings:
        listing.main_image = listing.images.all()[0].image

    return render(request, 'main/main.html', {'listings': listings})
