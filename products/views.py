from django.shortcuts import render, get_object_or_404
from products.models import Product

def shop_men(request):
    products_men = Product.objects.filter(category='men')
    return render(request, 'products/shop_men.html', {'products': products_men})

def shop_men_tshirts(request):
    tshirts = Product.objects.filter(category='men', subcategory='tshirt')
    return render(request, 'products/shop_men_tshirts.html', {'products': tshirts})

def shop_women(request):
    return render(request, 'products/shop_women.html')

def shop_accessories(request):
    return render(request, 'products/shop_accessories.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def shop_collection(request):
    return render(request, 'products/shop_collection.html')

