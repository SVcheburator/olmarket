from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('<int:category_id>', views.all_in_category, name='all_in_category'),
]