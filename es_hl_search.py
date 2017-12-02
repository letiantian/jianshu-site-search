# coding: utf-8

# 从 titile 和 content 中搜索，得到前 5 条结果
# 高亮 elasticsearch 搜索结果

import sys
from elasticsearch import Elasticsearch

if len(sys.argv) >= 2:
    keywords = ' '.join(sys.argv[1:])
else:
    print '''
    示例：
    python es_hl_search.py 人民的名义
    '''
    sys.exit(0)

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