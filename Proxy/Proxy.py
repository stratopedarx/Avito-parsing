# coding: utf-8
import requests
from lxml import html


class Proxy:
    result = []
    url = 'http://fineproxy.org/'

    def __init__(self):
        r = requests.get(self.url)
        res = html.fromstring(r.content)
        self.result = res.xpath("//div[@class='storycontent']/p/text()[position() >1]")

    def get_proxy(self):
        for proxy in self.result:
            url = 'http://' + proxy.strip()
            try:
                r = requests.get('http://www.google.ru/', proxies={'http': url})
                if r.status_code == 200:
                    return url
            except requests.exceptions.ConnectionError, requests.exceptions.ProxyError:
                continue

if __name__ == '__main__':
    proxy = Proxy()
    my_proxy = proxy.get_proxy()
    print my_proxy
    r = requests.get('http://speed-tester.info/check_ip.php', proxies={'http': my_proxy})
    print '='*80
    print r.content     # check proxy in html content

