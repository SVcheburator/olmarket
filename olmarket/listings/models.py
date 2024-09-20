from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from categories.models import Category

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.listing.title}"