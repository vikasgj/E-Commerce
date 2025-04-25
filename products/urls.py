from django.urls import path
from . import views

urlpatterns = [
    path('shop/men/', views.shop_men, name='shop_men'),
    path('shop/men/tshirts/', views.shop_men_tshirts, name='shop_men_tshirts'),
    path('shop/women/', views.shop_women, name='shop_women'),
    path('shop/accessories/', views.shop_accessories, name='shop_accessories'),
    path('shop/all/', views.all_products, name='all_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/collection/', views.shop_collection, name='shop_collection'),
]
