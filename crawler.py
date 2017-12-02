#coding:utf-8

'''
抓取某个用户的所有文章，按文章id将文章对应的网页保存到 data 目录。
'''
import os
import requests
import time
from bs4 import BeautifulSoup
import codecs
import sys

def extract_article_id_set(html_content):
    '''
    '''
    soup = BeautifulSoup(html_content, 'lxml')
    list_container = soup.find('div', id='list-container')
    result = set()
    for link in list_container.find_all('a', class_='title'):
        # print link.text, link.get('href')
        result.add(link.get('href').replace('/p/', ''))
    return result


def get_article_id_set(user):
    '''
    关于user：这里是指简书url中给出的ID。如
   
    http://www.jianshu.com/u/7fe2e7bb7d47?order_by=shared_at&page=10

    user 是 7fe2e7bb7d47
    '''
    page = 1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

    id_set = set()

    while True:
        url = 'http://www.jianshu.com/u/{0}?order_by=shared_at&page={1}'.format(user, page)
        print url
        resp = requests.get(url, headers=headers)
        # print resp.text
        result = extract_article_id_set(resp.text)
        if result.issubset(id_set):
            break
        else:
            id_set = id_set.union(result)
        print '-----------'
        page += 1
        time.sleep(2)
    return id_set


def download_articles(id_set):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

    dir_path = os.path.dirname(os.path.realpath(__file__))

    for article_id in id_set:
        url = 'http://www.jianshu.com/p/{0}'.format(article_id)
        print 'download {0}'.format(url)
        resp = requests.get(url, headers=headers)
        if (resp.status_code == 200):
            file_path = os.path.join(dir_path, 'data','{0}.html'.format(article_id))
            with codecs.open(file_path, 'w', encoding='utf-8') as f:
                print 'save'
                f.write(resp.text)
            time.sleep(1)




if __name__ == '__main__':
    if len(sys.argv) == 2:
        user_id = sys.argv[1]
        article_id_set = get_article_id_set(user_id)
        download_articles(article_id_set)
    else:
        print '''
            示例：
            python crawler.py 7fe2e7bb7d47
        '''