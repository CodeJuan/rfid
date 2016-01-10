# -*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html', RequestContext(request))


def vivian(request, filename):
    return render_to_response('%s.html' % filename, RequestContext(request))
