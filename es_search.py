# coding: utf-8

# 搜索

import sys
from elasticsearch import Elasticsearch

if len(sys.argv) >= 2:
    keywords = ' '.join(sys.argv[1:])
else:
    print '''
    示例：
    python es_search.py 人民的名义
    '''
    sys.exit(0)

es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

print '仅从 content 字段搜索，取前5条结果:'
result = es.search(index='jianshu', doc_type='ariticle', body={
    "query" : { "match" : { "content" : keywords }},
    "from": 0,
    "size": 5
})


for item in result['hits']['hits']:
    print 'url:   ', item['_source']['url']
    print 'title: ', item['_source']['title']
    print 'score: ', item['_score']
    print

print '-------------'
print

print '从 title 和 content 字段搜索，取前5条结果:'

result = es.search(index='jianshu', doc_type='ariticle', body={
    "query" : { 
        "bool": {
        "should": [
            {
                "match": {"title": keywords}
            },
            {
                "match": {"content": keywords}
            }
        ]
    }},
    "from": 0,
    "size": 5
})

for item in result['hits']['hits']:
    print 'url:   ', item['_source']['url']
    print 'title: ', item['_source']['title']
    print 'score: ', item['_score']
    print