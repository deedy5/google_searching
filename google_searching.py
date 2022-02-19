import unicodedata
from time import sleep

import requests
from lxml import html

__version__ = '0.8'

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"})


def ggl(keywords, lang='en', max_results=20):
    query  = keywords.replace(' ','+')
    results = []
    start = 0
    num = min(max_results + 5, 100)    

    while True:
        url = f'https://www.google.com/search?q={query}&num={num}&hl={lang}&start={start}&gbv=1'
        resp = session.get(url, timeout=10)
        
        if resp.status_code == 429:
            print('Сaptcha! Return None')
            return None
        
        if resp.status_code == 200:
            tree = html.fromstring(resp.text)
            elements = tree.xpath("//div[./div/a/h3]")
            
            if not elements:
                return results
            
            for e in elements:
                title = e.xpath('.//h3//text()')
                if title:
                    href = e.xpath('.//a/@href[1]')
                    body = e.xpath("./div[2]")
                    res = {            
                        'title': title[0],
                        'href': href[0].lstrip('/url?q=').split('&')[0],
                        'body': unicodedata.normalize("NFKD", body[0].text_content()) if body else "",
                        }
                results.append(res)
            
            if len(results) >= max_results or abs(max_results - len(results)) <= 10:
                return results
            
            start += num
        sleep(5)
