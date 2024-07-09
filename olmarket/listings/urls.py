from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('create_listing/', views.create_listing, name='create_listing'),
]