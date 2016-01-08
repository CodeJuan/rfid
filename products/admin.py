# -*- coding: utf-8-*-
from django.contrib import admin
from products.models import ProductStyle, ProductMaterial, ProductStatus
from products.models import ProductItem


@admin.register(ProductStyle, ProductMaterial, ProductStatus)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'desc')


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('product_photo', 'rfid', 'weight', 'style', 'material')

    fields = ('product_photo', 'rfid', 'weight',
              'name', 'status', 'style', 'material',
              'scale', 'notes')
    readonly_fields = ('product_photo', 'rfid', 'weight')

    def product_photo(self, ins):
        return '<img src="%s" title="%s"/>' % (
            ins.photo.url_150x150, ins.style)

    product_photo.short_description = "Product Photo Preview"
    product_photo.allow_tags = True
