from django.contrib import admin

# Register your models here.
from .models import Cart,Cartitem


admin.site.register(Cart)
admin.site.register(Cartitem)