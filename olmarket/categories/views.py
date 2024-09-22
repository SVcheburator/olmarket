from django.shortcuts import render

from listings.models import Listing
from categories.models import Category

# Create your views here.
def all_categories(request):
    categories = Category.objects.all()
    for category in categories:
        category.listings_amount = Listing.objects.filter(category=category).count
    return render(request, 'categories/all_categories.html', {'categories': categories})


def all_in_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category_listings = Listing.objects.filter(category=category)

    for listing in category_listings:
        listing.main_image = listing.images.all()[0].image

    return render(request, 'categories/all_in_category.html', {'category': category, 'category_listings': category_listings})