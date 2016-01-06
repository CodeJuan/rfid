#-*- coding:utf-8 -*-
from django.contrib import admin
from equipments.models import RfidReader, Ant


class RfidReaderAdmin(admin.ModelAdmin):
    list_display = ('shop', 'ip', 'port')

class AntAdmin(admin.ModelAdmin):
    list_display = ('reader', 'seq', 'mode')


admin.site.register(RfidReader, RfidReaderAdmin)
admin.site.register(Ant, AntAdmin)
