import time
import redis

def test():
    r = redis.Redis(host='192.168.1.245', port=6379, db=0)
    r.set('Hi', 'hello')
    r.expire('Hi',5)
    time.sleep(1)
    print r.get('Hi')
    time.sleep(8)
    print r.get('Hi')

if __name__ == '__main__':
    test()