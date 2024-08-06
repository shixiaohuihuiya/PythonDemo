import redis
import time
import threading

# 连接到 Redis 服务器
redis_conn = redis.Redis(host="localhost", port=6379, db=0, password="123456")


def producer(stream_name, messages):
    for message in messages:
        redis_conn.xadd(stream_name, {'message': message})
        print(f"Produced: {message}")
        time.sleep(1)  # 模拟生产延迟


def consumer(stream_name, group_name, consumer_name):
    # 创建消费者组
    try:
        redis_conn.xgroup_create(stream_name, group_name, '$', mkstream=True)
    except redis.exceptions.RedisError as e:
        if "BUSYGROUP Consumer Group name already exists" not in str(e):
            raise

    while True:
        # 从消费者组读取消息
        messages = redis_conn.xreadgroup(group_name, consumer_name, {stream_name: '>'}, count=1, block=1000)
        if messages:
            for stream, msg_list in messages:
                for msg_id, msg in msg_list:
                    print(f"Consumed: {msg[b'message'].decode('utf-8')}")
                    redis_conn.xack(stream_name, group_name, msg_id)


if __name__ == "__main__":
    messages = ["Hello, Stream!", "This is a test message.", "Another message."]

    # 创建生产者线程
    producer_thread = threading.Thread(target=producer, args=('mystream', messages))

    # 创建消费者线程
    consumer_thread = threading.Thread(target=consumer, args=('mystream', 'mygroup', 'consumer1'))

    # 启动线程
    producer_thread.start()
    consumer_thread.start()

    # 等待线程完成
    producer_thread.join()
    consumer_thread.join()
