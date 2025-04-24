from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),  # Newsletter subscription
]
