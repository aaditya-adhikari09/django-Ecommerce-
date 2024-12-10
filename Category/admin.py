from django.contrib import admin
from .models import Category


class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}
    list_display = ('category','slug')
# Register your models heg
admin.site.register(Category,Categoryadmin)

