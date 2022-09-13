from django.contrib import admin

from .models import *


class CartDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'product_name', 'product_quantity')


class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'price')


class PostSaveAdmin(admin.ModelAdmin):
    list_display = ('entry', 'created')


admin.site.register(CartData, CartDataAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
admin.site.register(PostSave, PostSaveAdmin)
