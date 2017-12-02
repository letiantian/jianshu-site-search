#coding: utf-8
import os
import sys
import codecs
from bs4 import BeautifulSoup


def as_unicode(text):
    try:
        return text.decode('utf-8')
    except:
        return text

dir_path = os.path.dirname(os.path.realpath(__file__))

keywords = sys.argv[1:]
print '你输入了：', ' '.join(keywords)


KEY_URL     = 'KEY_URL'
KEY_TITLE   = 'KEY_TITLE'
KEY_CONTENT = 'KEY_CONTENT'
KEY_SCORE   = 'KEY_SCORE'

data = []

for filename in os.listdir(os.path.join(dir_path, 'data')):
    if filename.endswith('.html'):
        item = {}
        article_id = filename.replace('.html', '')
        item[KEY_URL] = 'http://www.jianshu.com/p/{0}'.format(article_id)
        html_content = codecs.open(os.path.join(dir_path, 'data', filename), 'r', encoding='utf-8').read()
        soup = BeautifulSoup(html_content, 'lxml')
        item[KEY_TITLE] = soup.find('h1', class_='title').text
        item[KEY_CONTENT] = soup.find('div', class_='show-content').text

        item[KEY_URL] = as_unicode(item[KEY_URL])
        item[KEY_TITLE] = as_unicode(item[KEY_TITLE])
        item[KEY_CONTENT] = as_unicode(item[KEY_CONTENT])
        item[KEY_SCORE] = 0

        data.append(item)


# 开始搜索
result = []
for item in data:
    for kw in keywords:
        kw = as_unicode(kw)
        # if kw.lower() in item[KEY_TITLE].lower() or kw.lower() in item[KEY_CONTENT].lower():
        #     print '命中了： ', item[KEY_URL] 
        if kw.lower() in item[KEY_TITLE].lower():
            item[KEY_SCORE] += 2
        if kw.lower() in item[KEY_CONTENT].lower():
            item[KEY_SCORE] += 1
    if item[KEY_SCORE] > 0:
        result.append(item)

# 排序输出
print '搜索结果：'
for item in sorted(result, key=lambda item: item[KEY_SCORE], reverse=True):
    print
    print 'url:   ', item[KEY_URL]
    print 'title: ', item[KEY_TITLE]
    print 'score: ', item[KEY_SCORE]
    

