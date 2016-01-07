# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from products.api import RFIDResource

urlpatterns = patterns('',
    url(r'^$', 'base.views.home', name='home'),
    url(r'^vivian', 'base.views.vivian', name='vivian'),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^shops/',  include('shops.urls')),
    url(r'^products/', 'products.views.report_rfid'),
    url(r'^getproducts/', 'products.views.get_all_rfid'),
    url(r'^api/', include(RFIDResource().urls)),
    url(r'^api/v1/report/$', 'monitor.views.post_report'),
    url(r'^api/products/checkin', 'products.views.checkin'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,
             }
            ),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT,
             }
            ),
    )
