# -*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from shops.models import Shop


def shop_list(request):
    content = {
        'shops': Shop.objects.all(),
        }
    return render_to_response('shops.html', RequestContext(request, content))
