# 编写第一个网络爬虫
from urllib3 import *
from re import *
http = PoolManager()
disable_warnings()

def download(url):
    result = http.request('GET', url)
    htmlStr = result.data.decode('utf-8')
    return htmlStr

def analyse(htmlStr):
    # <a href='a.html'>a</a>
    aList = findall('<a[^>]*>',htmlStr)
    result = []
    for a in aList:
        # <a href='a.html'>
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]',a)
        if g != None:
            url = g.group(1)
            url = 'http://localhost:8888/files/' + url
            result.append(url)
    return result

def crawler(url):
    print(url)
    html = download(url)
    urls = analyse(html)
    for url in urls:
        crawler(url)
crawler('http://localhost:8888/files')