# coding: utf-8

# 高亮搜索结果

from elasticsearch import Elasticsearch


keywords = '人民的名义'

es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

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
        }
    },
    "highlight": {
        "fields" : {
            "title" : {},
            "content": {}
        }
    },
    "from": 0,
    "size": 5
})

print 'title & content:'
for item in result['hits']['hits']:
    print item['_source']['url']
    print item['_source']['title']
    print ' '.join(item['highlight']['content'][:4])
    print item['_score']
    print