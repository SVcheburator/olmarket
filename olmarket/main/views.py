from django.shortcuts import render

from listings.models import Listing
from categories.models import Category

# Create your views here.
def main(request):
    categories = Category.objects.all()
    category_listings = {}
    
    for category in categories:
        listings_in_category = Listing.objects.filter(category=category)[:4]
        category_listings[category] = listings_in_category

    return render(request, 'main/main.html', {'category_listings': category_listings})
