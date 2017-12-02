# coding: utf-8

# 创建 jianshu 索引，指定 document 类型

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

body = {
    "mappings" : {
        "ariticle" : {
            "properties" : {
                "url" : {                 # url 
                    "type" : "text"
                },
                "title" : {               # 标题
                    "type" : "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "content" : {             # 正文
                    "type" : "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word" 
                }
            }
        }
    }
}

es.indices.create(index='jianshu', body=body)

