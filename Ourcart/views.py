from django.shortcuts import render
from store.models import Product
def home(request):
    products = Product.objects.all().filter(is_available = True)
    return render(request,'home.html')

    #   context = {
    #     'products':products,
    # }
    # return render(request,'home.html',context)
