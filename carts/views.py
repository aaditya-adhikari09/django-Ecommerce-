from django.shortcuts import render ,redirect,get_object_or_404
from store.models import Product
from carts.models import Cart,Cartitem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# from django.shortcuts import render
from . import views
def cart(request,total = 0,quantity = 0, cart_item = None):
    try :
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = Cartitem.objects.filter(cart = cart, is_active =True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total/100)
        grand_total = total +tax

    except ObjectDoesNotExist:
        cart_items = []

    context ={
        'total': total ,
        'quantity' : quantity,
        'cart_items': cart_items,
        'tax' : tax ,
        'grand_total' : grand_total ,}
    # return render(request,'store/cart.html')
    return render(request,'cart.html',context)
    
def _cart_id(request):
    cart = request.session.session_key 
    if not cart :
        cart = request.session.create()
    return cart 

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try :
        cart = Cart.objects.get(cart_id =_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try :
        cart_item = Cartitem.objects.get(product=product,cart =cart)
        cart_item.quantity += 1
        cart_item.save()

    except Cartitem.DoesNotExist:
        cart_item = Cartitem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    
    # exit()
    return redirect('cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id =_cart_id(request))
    product = get_object_or_404(Product,id = product_id)
    cart_item = Cartitem.objects.get(product=product,cart = cart)
    if cart_item.quantity > 1 :
        cart_item.quantity -= 1 
        cart_item.save()
    else :
        cart_item.delete()
    return redirect('cart')

# def remove_cart_item(request,product_id):
#     cart = Cart.objects.get(cart_id =_cart_id(request))
#     product = get_object_or_404(Product,id = product_id)
#     cart_item = Cartitem.objects.get(product = product, cart = cart)
#     cart_item.delete()
#     return redirect('cart')
def continueshopping(request):
    return render(request,'store.html')
