from django.contrib import admin
from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    path('cart/<int:p>', views.cart, name = "cart"),
    path('cart_view', views.cart_view, name = "cart_view"),
    path('cart_remove/<int:p>', views.cart_remove, name = "cart_remove"),
    path('full_remove/<int:p>', views.full_remove, name = "full_remove"),
    path('orderform/', views.order, name = "orderform"),
    path('orderview/', views.orderview, name = "orderview"),
]
