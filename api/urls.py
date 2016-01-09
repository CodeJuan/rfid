#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = (
    url(r'^auth', 'api.views.auth', name='api_auth'),
)
