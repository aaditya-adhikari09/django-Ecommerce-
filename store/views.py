from django.shortcuts import render, get_object_or_404
from .models import Product, Category 
from carts.views import _cart_id
from django.http import HttpResponse
from carts.models import Cartitem
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def store(request, category_slugs=None):
    categories= None
    products = None
    if category_slugs != None:
        # Fetch category using slug and get products in that category
        category = get_object_or_404(Category, slug=category_slugs)
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        product_count = products.count()
        # product_count = products.count()
    else:
        # Get all available products
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products,6)
        page  =request.GET.get('page')
        paged_products = paginator.get_page('page')
        product_count = products.count()



    context = {
        'products': products,
    }
    return render(request, 'store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug = product_slug)
        in_cart = Cartitem.objects.filter(cart__cart_id=_cart_id(request),product = single_product).exists()
        return HttpResponse(in_cart)
        exit
    except Exception as e :
        raise e
        
    context = {
        'single_product':single_product,
        'in_cart' : in_cart,
    }
    return render(request,'product_detail.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword =request.GET['keyword']
        if keyword :
            products = Product.objects.order_by('-created_date').filter(description__icontains=keyword )
        context ={
            'products': products,
        }
    return render(request,'store.html',context)