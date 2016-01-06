#-*- coding:utf-8 -*-
from django.contrib import admin
from equipments.models import RfidReader, Ant


class RfidReaderAdmin(admin.ModelAdmin):
    list_display = ('IP', 'port', 'loc')

class AntAdmin(admin.ModelAdmin):
    list_display = ('seq', 'reader', 'status')


admin.site.register(RfidReader, RfidReaderAdmin)
admin.site.register(Ant, AntAdmin)
