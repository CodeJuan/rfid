#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response


def shop_list(request):
    content = {
        }
    return render_to_response('shops.html', RequestContext(request, content))
