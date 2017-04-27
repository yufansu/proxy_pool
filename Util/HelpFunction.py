import requests
from time import sleep
from lxml import etree


def getHTMLTree(url):
    header = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    if "www.kuaidaili.com" in url:
        sleep(1)

    r = requests.get(url=url, headers=header, timeout=30)
    html = r.content
    HTMLTree = etree.HTML(html)
    return HTMLTree
