from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('all_in_category/<int:category_id>', views.all_in_category, name='all_in_category'),
]