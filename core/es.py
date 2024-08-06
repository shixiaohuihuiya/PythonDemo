from elasticsearch import Elasticsearch

class NodeConfig:
    def __init__(self, host, port, scheme):
        self.host = host
        self.port = port
        self.scheme = scheme

# 定义连接选项
options = {
    'host': 'localhost',
    'port': 9200,
    'scheme': 'http'  # 确保包含 scheme 参数
}

# 初始化 NodeConfig 对象
node_config = NodeConfig(**options)  # type: ignore

# 创建 Elasticsearch 客户端实例
es = Elasticsearch([{
    'host': node_config.host,
    'port': node_config.port,
    'scheme': node_config.scheme
}])

# 检查连接
if es.ping():
    print("Successfully connected to Elasticsearch!")
else:
    print("Failed to connect to Elasticsearch.")
