from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'stock', 'created_at', 'updated_at')
    search_fields = ('title', 'category')
    list_filter = ('category',)
