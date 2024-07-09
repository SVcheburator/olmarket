from django import forms
from .models import Listing, ListingImage
from .widgets import MultiFileInput


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'category']


class ListingImageForm(forms.ModelForm):
    class Meta:
        model = ListingImage
        fields = ['image']

    image = forms.ImageField(widget=MultiFileInput)
