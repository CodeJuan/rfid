import time
from django.test import TestCase
import requests
import urllib2
import json
from json import JSONEncoder
import redis

def test():
    r = redis.Redis(host='192.168.1.245', port=6379, db=0)
    print r.get('22222222')
    time.sleep(8)
    print r.get('22222222')

def testPostReport():
    print 'aaaa'
    headers = {'content-type': 'application/json'}
    payload = {"AntennaID": "55555555", "RFID": "22222222"}
    r = requests.post('http://localhost:8000/api/v1/report/', data=json.dumps(payload), headers=headers)
    print r.status_code
    print r.json()

def testCheckIn():
    print 'CheckIn'
    headers = {'content-type': 'application/json'}
    payload = {'RFID': '555555555',
                'AntennaID': '222222222',
                'User': 'xiong',
                'Shop': 1,
                'Weight': 1.01}
    r = requests.post('http://localhost:8000/api/products/checkin/', data=json.dumps(payload), headers=headers)
    print r.status_code
    print r.json()

if __name__ == '__main__':
    #testPostReport()
    #test()
    testCheckIn()