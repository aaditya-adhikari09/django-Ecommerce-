from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def store(request, category_slugs=None):
    if category_slugs:
        # Fetch category using slug and get products in that category
        category = get_object_or_404(Category, slug=category_slugs)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        # Get all available products
        products = Product.objects.filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug = product_slug)
    except Exception as e :
        raise e
    context = {
        'single_product':single_product
    }
    return render(request,'product_detail.html',context)