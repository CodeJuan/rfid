from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from monitor.models import Report
from monitor.serializers import ReportSerializer
import redis


@api_view(['POST'])
def post_report(request):
    print 'post_report'
    if request.method == 'POST':
        rfid = request.data.get('RFID')
        data = {'RFID': rfid, 'AntennaID': request.data.get('AntennaID')}
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            r = redis.Redis(host='192.168.1.245', port=6379, db=0)
            r.set(rfid, '1')
            r.expire(rfid, 15)
            return Response(serializer.data, status=status.HTTP_201_CREATED)