#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from products import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.ProductItemList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductItemDetail.as_view()),
])
