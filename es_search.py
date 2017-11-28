# coding: utf-8

# 搜索

from elasticsearch import Elasticsearch


keywords = '人民的名义'

es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

result = es.search(index='jianshu', doc_type='ariticle', body={
    "query" : { "match" : { "content" : keywords }},
    "from": 0,
    "size": 5
})

print 'only content:'
for item in result['hits']['hits']:
    print item['_source']['url']
    print item['_source']['title']
    print item['_score']
    print

print '-------------'
print

result = es.search(index='jianshu', doc_type='ariticle', body={
    "query" : { 
        "bool": {
        "should": [
            {
            "match": {
                "title": keywords
            }
            },
            {
            "match": {
                "content": keywords
            }
            }
        ]
    }},
    "from": 0,
    "size": 5
})

print 'title & content:'
for item in result['hits']['hits']:
    print item['_source']['url']
    print item['_source']['title']
    print item['_score']
    print