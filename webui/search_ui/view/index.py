# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from elasticsearch import Elasticsearch

def _(request):
    keywords = request.GET.get('keywords', '').strip()
    if keywords == '':
        return render(request, 'index.html', {
            'title': '简书站内搜索', 
            'keywords': keywords,
            'err_info': '',
            'result': [],
            })
    else:
        result = get_elastic_search_result(keywords)
        if len(result) == 0:
            return render(request, 'index.html', {
                'title': '简书站内搜索', 
                'keywords': keywords,
                'err_info': '无内容',
                'result': [],
                })
        else:
            return render(request, 'index.html', {
                'title': '简书站内搜索', 
                'keywords': keywords,
                'err_info': '仅显示最多5条结果',
                'result': result,
                })


def get_elastic_search_result(keywords):
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
    
    return [{'url':item['_source']['url'], 
             'title':mark_safe(' '.join(item['highlight']['title'])), 
             'content':mark_safe(' '.join(item['highlight']['content']))} 
             for item in result['hits']['hits']]