from django.http import HttpResponse
from django.shortcuts import render_to_response
from products.models import RFID
# Create your views here.

def report_rfid(request):
    rfid = RFID(RFID='123456789012', AntennaID= '1111122222')
    rfid.save()
    return HttpResponse("ok")

def get_all_rfid(request):
    all = RFID.objects.all()
    for rfid in all:
        print rfid.RFID, rfid.AntennaID
    return render_to_response('all_rfids.html', {'rfids': all})