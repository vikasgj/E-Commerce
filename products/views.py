from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from products.models import Product

# View for men's products
def shop_men(request):
    # Logic for retrieving men's products from the database (e.g., Product model)
    products_men = Product.objects.filter(category='men')  # Adjust according to your model
    return render(request, 'products/shop_men.html', {'products': products_men})

# Create a view for the women's products page
def shop_women(request):
    # Logic to display women's products
    return render(request, 'products/shop_women.html')

# Create a view for the accessories products page
def shop_accessories(request):
    # Logic to display accessories products
    return render(request, 'products/shop_accessories.html')

# View for displaying all products
def all_products(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'products/all_products.html', {'products': products})

# View for displaying product details
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by its ID
    return render(request, 'products/product_detail.html', {'product': product})

def shop_collection(request):
    return render(request, 'products/shop_collection.html')  # or whatever template you're using
