
import redis
pool=redis.ConnectionPool(host='127.0.0.1',
                          port=6379,db=0)
r=redis.StrictRedis(connection_pool=pool)

data = [1,2,3]
while True:
    msg=input("publish: >>")
    if msg=="over":
        print("停止发布")
        r.publish('spub',)
        break
    r.publish('spub', data)
