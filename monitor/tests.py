import time
from django.test import TestCase
import requests
import urllib2
import json
from json import JSONEncoder
import redis
from django.conf import settings

def test():
    r = redis.Redis(host='localhost', port=6379, db=0)
    #r = redis.Redis(host=settings.REDIS_ADDR, port=settings.REDIS_PORT, password= settings.REDIS_PASSWORD,db=0)
    print r.get('22222222')
    time.sleep(16)
    print r.get('22222222')

def testPostReport():
    print 'aaaa'
    headers = {'content-type': 'application/json'}
    payload = [{"RFID": "22222222"},{"RFID": "111111"}]
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
    testPostReport()
    test()
    # testCheckIn()