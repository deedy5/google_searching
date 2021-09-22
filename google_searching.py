from time import sleep

import requests
from lxml import html

__version__ = 0.3

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"})

def ggl(keywords, max_results=20):
    query  = keywords.replace(' ','+')
    results = []
    num = min(max_results, 100)
    start = 0
    while True:
        url = f'https://www.google.com/search?q={query}&num={max_results}&hl=en&&start={start}'
        resp = session.get(url, timeout=5)
        if resp.status_code == 429:
            print('Сaptcha! Return None')
            return None
        if resp.status_code == 200:
            tree = html.fromstring(resp.text)
            temp_results = []
            elements = tree.xpath("//div[@class='g']")
            if not elements:
                return results
            for g in elements:
                snippets = g.xpath('.//div/div/div[2]/div')
                snippet = None
                rich_snippet = None
                if len(snippets) == 1:
                    snippet = snippets[0].text_content()
                elif len(snippets) > 1:
                    if len(snippets[1].xpath('.//g-review-stars')) > 0:
                        rich_snippet = snippets[1].text_content()
                        snippet = snippets[0].text_content()
                    else:
                        snippet = snippets[1].text_content()
                        rich_snippet = snippets[0].text_content()
                res = {            
                    'title': g.xpath('.//h3/text()')[0],
                    'href': g.xpath('.//@href[1]')[0],
                    'body': snippet,
                    'rich_body': rich_snippet,
                    }
                temp_results.append(res)

            start += num
            results.extend(temp_results)
            if len(results) >= max_results or abs(max_results - len(results)) <= 10:
                return results
            sleep(5)
