#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = (
    url(r'^$', 'shops.views.shop_list', name='shops_home'),
)
