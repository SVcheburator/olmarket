from django.shortcuts import render

from listings.models import Listing, Category

# Create your views here.
def main(request):
    all_listings = Listing.objects.all()
    for listing in all_listings:
        listing.main_image = listing.images.all()[0].image

    categories = Category.objects.all()
    category_listings = {}
    for category in categories:
        listings_in_category = Listing.objects.filter(category=category)
        category_listings[category] = listings_in_category

    return render(request, 'main/main.html', {'all_listings': all_listings,'category_listings': category_listings})
