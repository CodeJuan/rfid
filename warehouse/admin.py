# -*- coding: utf-8-*-
from django.contrib import admin
from warehouse.models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'addr', 'addr', 'contact', 'phone', 'status')


admin.site.register(Warehouse, WarehouseAdmin)
