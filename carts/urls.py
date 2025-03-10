from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/',views.remove_cart,name = 'remove_cart'),
    path('store',views.continueshopping,name='store'),
    # path('remove/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    # path('remove_cart_item/<int:product_id>/',views.remove_cart_item,name = 'remove_cart_item'),
    # path('remove_cart_item/<int:product_id>/',views.remove_cart_item,name='remove_cart_item'),
]
