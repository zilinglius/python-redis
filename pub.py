import io
from PIL import Image
import redis

pool=redis.ConnectionPool(host='127.0.0.1',
                          port=6379,db=0)
r=redis.StrictRedis(connection_pool=pool)

img = Image.open('test.jpg', mode='r')
imgByteArr = io.BytesIO()
img.save(imgByteArr, format='JPEG')
imgByteArr = imgByteArr.getvalue()

data = bytes('http://www.baidu.com', )

r.publish('spub', imgByteArr)

while True:
    msg=input("publish: >>")
    if msg=="over":
        print("停止发布")
        r.publish('spub',)
        break
    r.publish('spub', imgByteArr)
