from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from monitor.models import Report
from monitor.serializers import ReportSerializer
import os
import redis
from django.conf import settings

#redis = redis.Redis(host=os.environ['REDIS_PORT_6379_TCP_ADDR'],
#              port=os.environ['REDIS_PORT_6379_TCP_PORT'],
#              password=os.environ.get('REDIS_PASSWORD'))
#redis = redis.Redis(host='localhost', port=6379, db=0)
redis = redis.Redis(host=settings.REDIS_ADDR, port=settings.REDIS_PORT, password= settings.REDIS_PASSWORD,db=0)
@api_view(['POST'])
def post_report(request):
    try:
        for data in request.data:
            print data
            rfid = data
            redis.set(rfid, '1')
            redis.expire(rfid, 15)

        return Response(request.data, status=status.HTTP_201_CREATED)
    except:
        return Response('error', status=status.HTTP_400_BAD_REQUEST)