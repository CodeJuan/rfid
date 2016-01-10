import requests
import json
from django.core.cache import cache
import time
import sys

def test():
    port = str(sys.argv[1])
    url = 'http://localhost:{}/products/'.format(port)
    print url
    while True:
        r = requests.get(url)
        data = json.loads(r.text)
        lost = []
        for rfid in data:
            cur = rfid['rfid']
            if cache.get(cur) == None:
                lost.append(cur)

        cache.set('lost', lost)
        time.sleep(3*60)

if __name__ == '__main__':
    test()