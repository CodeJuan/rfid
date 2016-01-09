import requests
import json
import redis
from django.conf import settings
# Create your tests here.
redis = redis.Redis(host=settings.REDIS_ADDR, port=settings.REDIS_PORT, password= settings.REDIS_PASSWORD,db=0)

def test():
    r = requests.get('http://localhost:8000/products/ProductItems')
    print r.text
    data = json.loads(r.text)
    lost = []
    for rfid in data:
        cur = rfid['RFID']
        if redis.get(cur) == None:
            print 'lost',cur
            lost.append(cur)

    redis.set('lost', lost)
    print redis.get('lost')

if __name__ == '__main__':
    test()