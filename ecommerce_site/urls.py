from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include the core app URLs
    path('products/', include('products.urls')),  # Products app URLs
    path('wishlist/', include('wishlist.urls')),  # Wishlist app URLs
    path('orders/', include('orders.urls')),  # Orders app URLs
]

# Serve media and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Corrected line
