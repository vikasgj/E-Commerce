# wishlist/views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Wishlist
from products.models import Product

def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist:all_wishlist')  # Adjust redirect based on your URL structure
