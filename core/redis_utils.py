# -*- coding: UTF-8 -*-
# author:xiaohuihui
# time : 2024/8/3 2:59
# file: redis_utils.py
# software: PyCharm
import redis

# 创建redis的连接

redis_conn = redis.Redis(host="localhost",port=6379,db=3,password=123456)


# 生产者函数
def producer(query_name,message):
    redis_conn.lpush(query_name,message)
    print(f"Produced: {message}")

# 消费者代码
def consumer(stream_name,group_name,sonsumer_name):
    # 创建消费者组
    try:
        redis_conn.xgroup_create(stream_name,group_name,'$',mkstream=True)
    except redis.exceptions.RedisError as e:
        if "BUSYGROUP Consumer Group name already exists" not in str(e):
            raise

    while True:
        # 从消费者中读取消息
        messages = redis_conn.xreadgroup(group_name,sonsumer_name,{stream_name:'>'},count = 1,block=1000)
        if messages:
            for stream,msg_list in messages:
                for msg_id , msg in msg_list:
                    print(f"Consumed: {msg[b'message'].decode('utf-8')}")
                    redis_conn.xack(stream_name, group_name, msg_id)




if __name__ == '__main__':
    producer("hch","hello world!")
    consumer('mystream', 'mygroup', 'consumer1')