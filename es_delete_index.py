# coding: utf-8

# 删除索引

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])


es.indices.delete(index='jianshu')