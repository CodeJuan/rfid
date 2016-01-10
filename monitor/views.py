# -*- coding:utf-8 -*-
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json


@api_view(['POST'])
def report_rfid(request):
    for item in request.data:
        rfid, ant, ip = item.split(',')
        cache.set(rfid, '', timeout=settings.RFID_LIFETIME)
        cache.set('-'.join([ant, ip]), '', timeout=settings.RFID_LIFETIME)
    return HttpResponse('ok')
