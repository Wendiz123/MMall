from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartItem)

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 3

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)