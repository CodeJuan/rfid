#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = (
    url(r'^auth', 'api.views.auth', name='api_auth'),
    url(r'^report_rfid', 'monitor.views.report_rfid', name='report_rfid'),
)
