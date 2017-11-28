# coding: utf-8

# 创建索引和type

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

body = {
    "mappings" : {
        "ariticle" : {
            "properties" : {
                "url" : { 
                    "type" : "text"
                },
                "title" : { 
                    "type" : "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "content" : { 
                    "type" : "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word" 
                }
            }
        }
    }
}

es.indices.create(index='jianshu', body=body)

