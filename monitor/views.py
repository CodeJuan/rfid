# -*- coding:utf-8 -*-
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def report_rfid(request):
    for rfid in request.data:
        cache.set(rfid, '', timeout=settings.RFID_LIFETIME)
    return HttpResponse('ok')
