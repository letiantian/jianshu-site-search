# coding: utf-8

# 将爬虫抓取的数据导入到es中

import os
import sys
import codecs
from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup

def process_text(text):
    ''' 将换行、多个空格替换成一个空格 '''
    text = text.strip().replace('\n', ' ')
    return ' '.join(text.split())


dir_path = os.path.dirname(os.path.realpath(__file__))

es = Elasticsearch([{'host':'127.0.0.1', 'port': 9200}])

## 下面这种方式无法避免一篇文章被索引多次
'''
for filename in os.listdir(os.path.join(dir_path, 'data')):
    if filename.endswith('.html'):
        print filename
        file_path = os.path.join(dir_path, 'data', filename)
        article_id = filename.replace('.html', '')
        url = 'http://www.jianshu.com/p/{0}'.format(article_id)
        html_content = codecs.open(file_path, 'r', encoding='utf-8')
        soup = BeautifulSoup(html_content, 'lxml')
        title = soup.find('h1', class_='title').text
        content = soup.find('div', class_='show-content').text
        es.index(index='jianshu', doc_type='ariticle', body={
            'url': url,
            'title': process_text(title),
            'content': process_text(content)
        })
'''

## 用 article id 作为 id，以避免一篇文章被索引多次
for filename in os.listdir(os.path.join(dir_path, 'data')):
    if filename.endswith('.html'):
        print filename
        file_path = os.path.join(dir_path, 'data', filename)
        article_id = filename.replace('.html', '')
        url = 'http://www.jianshu.com/p/{0}'.format(article_id)
        html_content = codecs.open(file_path, 'r', encoding='utf-8')
        soup = BeautifulSoup(html_content, 'lxml')
        title = soup.find('h1', class_='title').text
        content = soup.find('div', class_='show-content').text
        es.index(index='jianshu', doc_type='ariticle', id=article_id, body={
            'url': url,
            'title': process_text(title),
            'content': process_text(content)
        })