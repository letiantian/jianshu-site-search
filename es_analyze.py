# coding: utf-8

# 分词

import uniout
from elasticsearch import Elasticsearch

keywords = '人民的名义'

es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

print es.indices.analyze(index='jianshu', body={
        "analyzer" : "standard",
        "text" : keywords
    })

print 'standard:'
print es.indices.analyze(index='jianshu', body={
        "analyzer" : "standard",
        "text" : keywords
    })

print 

print 'ik_max_word:'
print es.indices.analyze(index='jianshu', body={
        "analyzer" : "ik_max_word",
        "text" : keywords
    })