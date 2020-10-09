
import redis
pool=redis.ConnectionPool(host='127.0.0.1',
                          port=6379,db=0)
r=redis.StrictRedis(connection_pool=pool)
while True:
    msg=input("publish: >>")
    if msg=="over":
        print("停止发布")
        break
    r.publish('spub',msg)
