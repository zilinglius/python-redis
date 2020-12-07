import io
from PIL import Image
import redis
import time

pool=redis.ConnectionPool(host='127.0.0.1',
                          port=6379,db=0)
r=redis.StrictRedis(connection_pool=pool)

img = Image.open('test.jpg', mode='r')

start_time = time.time()
imgByteArr = io.BytesIO()
img.save(imgByteArr, format='JPEG')
imgByteArr = imgByteArr.getvalue()
id = '102-' + '{:.3f}'.format(time.time())
data = bytes(id, encoding = 'utf8') + imgByteArr
end_time = time.time()
print('time cost',end_time - start_time,'ms')

r.publish('spub', data)

while True:
    msg=input("publish: >>")
    if msg=="over":
        print("停止发布")
        r.publish('spub', msg)
        break
    r.publish('spub', data)
