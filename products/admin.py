# -*- coding: utf-8-*-
from django.contrib import admin
from products.models import ProductStyle, ProductMaterial, ProductStatus
from products.models import ProductItem
from products.models import OpType
from products.models import ShopIn, ShopOut, ShelfOnOff


@admin.register(ProductStyle, ProductMaterial, ProductStatus)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'desc')


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = (
        'product_photo', 'style', 'name', 'material',
        'rfid', 'weight', 'scale', 'status',
        )

    fields = (('photo', 'product_photo'), 'rfid', 'weight',
              'name', 'status', 'style', 'material',
              'scale', 'notes', 'shop',
              )
    readonly_fields = ('product_photo', )  # 'rfid', 'weight')

    def product_photo(self, ins):
        return '<img src="%s" title="%s"/>' % (
            ins.photo.url_200x200, ins.style)

    product_photo.short_description = "Preview"
    product_photo.allow_tags = True


@admin.register(OpType)
class OpTypeAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'desc')


@admin.register(ShopIn, ShopOut, ShelfOnOff)
class OperationAdmin(admin.ModelAdmin):
    list_display = (
        'tracking_no', 'rfid', 'get_prod_name',
        'get_prod_style', 'get_prod_material',
        'get_prod_weight', 'get_prod_scale',
        'op_type', 'operator', 'update_time',
        )

    def get_prod_name(self, obj):
        return obj.product.name

    get_prod_name.short_description = "物件名称"
    get_prod_name.allow_tags = True

    def get_prod_style(self, obj):
        return obj.product.style

    get_prod_style.short_description = "款式"
    get_prod_style.allow_tags = True

    def get_prod_material(self, obj):
        return obj.product.material

    get_prod_material.short_description = "材质"
    get_prod_material.allow_tags = True


    def get_prod_weight(self, obj):
        return obj.product.weight

    get_prod_weight.short_description = "重量 (g)"
    get_prod_weight.allow_tags = True

    def get_prod_scale(self, obj):
        return obj.product.scale

    get_prod_scale.short_description = "尺寸 (mm)"
    get_prod_scale.allow_tags = True
