from django.http import HttpResponse
from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import RFID
from products.models import CheckIn
from products.serializers import CheckinSerializer
from products.models import ProductItem
import json
# Create your views here.

def report_rfid(request):
    #rfid = RFID(RFID='123456789012', AntennaID= '1111122222')
    rfid = ProductItem(rfid='1111111111')
    rfid.save()
    return HttpResponse("ok")


def get_all_rfid(request):
    all = RFID.objects.all()
    for rfid in all:
        print rfid.RFID, rfid.AntennaID
    return render_to_response('all_rfids.html', {'rfids': all})


@api_view(['POST'])
def checkin(request):
    print 'checkin'
    if request.method == 'POST':
        data = {'RFID': request.data.get('RFID'),
                'AntennaID': request.data.get('AntennaID'),
                'User': request.data.get('User'),
                'Shop': request.data.get('Shop'),
                'Weight': request.data.get('Weight')}
        print data
        serializer = CheckinSerializer(data=data)
        print serializer
        if serializer.is_valid():
            serializer.save()
            print 'save'
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response('error', status=status.HTTP_400_BAD_REQUEST)


def getProductItems(request):
    print 'getProductItems'
    all = ProductItem.objects.all()
    payload = []
    for product in all:
        payload.append({u'RFID':product.rfid})
    print payload
    headers = {'content-type': 'application/json'}
    data=json.dumps(payload)
    print data
    res = HttpResponse(data, status=status.HTTP_200_OK)
    return res