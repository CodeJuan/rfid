#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = (
    #url(r'^/products$', 'products.views.report_rfid'),
    url(r'^$', 'products.views.report_rfid', name=''),
    #url(r'^getproducts/', 'products.views.get_all_rfid'),
    url(r'^ProductItems$', 'products.views.getProductItems', name='ProductItems'),
)
