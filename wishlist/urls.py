# wishlist/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # Add other wishlist related URLs here
]
