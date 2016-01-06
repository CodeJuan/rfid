# -*- coding: utf-8-*-
from django.contrib import admin
from shops.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'addr', 'admin', 'contact', 'phone', 'status')


admin.site.register(Shop, ShopAdmin)
