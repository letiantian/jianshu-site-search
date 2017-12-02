# coding: utf-8

# 分词

import sys
import uniout
from elasticsearch import Elasticsearch

if len(sys.argv) >= 2:
    keywords = ' '.join(sys.argv[1:])
else:
    print '''
    示例：
    python es_analyze.py 人民的名义
    '''
    sys.exit(0)



es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

print 'standard 分词:'
print es.indices.analyze(index='jianshu', body={
        "analyzer" : "standard",
        "text" : keywords
    })

print 

print 'ik_max_word 分词:'
print es.indices.analyze(index='jianshu', body={
        "analyzer" : "ik_max_word",
        "text" : keywords
    })