from django.test import TestCase
import requests
import urllib2
import json
from json import JSONEncoder

# Create your tests here.

def test():
    print 'aaaa'
    headers = {'content-type': 'application/json'}
    payload = {"AntennaID": "55555555", "RFID": "22222222"}
    r = requests.post('http://localhost:8000/api/rfid/', data=json.dumps(payload), headers=headers)
    print r.status_code

#    data = {"AntennaID": "55555555", "RFID": "22222222"}
#    req = urllib2.Request('http://localhost:8000/api/rfid')
#    req.add_header('Content-Type', 'application/json')
#    response = urllib2.urlopen(req, json.dumps(data))


if __name__ == '__main__':
    test()