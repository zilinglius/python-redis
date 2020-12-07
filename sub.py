import os
import io
from PIL import Image
import redis

pool=redis.ConnectionPool(host='127.0.0.1',
                          port=6379,db=0)

r=redis.StrictRedis(connection_pool=pool)
p=r.pubsub()
p.subscribe("spub","cctv1")

for item in p.listen():
    print("Listen on channel : %s "%item['channel'].decode())
    if item['type']=='message':
        if len(item['data']) > 4 :
            with open('received.jpg', 'wb') as f:
                id=item['data'][:18]
                print(id)
                f.write(item['data'][19:])
        elif len(item['data']) == 4 and item['data'].decode()=='over':
            print(item['channel'].decode(),'停止发布')
            break
p.unsubscribe('spub')
print("取消订阅")
