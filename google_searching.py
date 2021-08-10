from lxml import html
import requests

__version__ = 0.1

def get_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    url = f"https://{url}" if ('https://' not in url) else url
    resp = requests.get(url, headers=headers, timeout=5)
    if resp.status_code == 200:
        return resp
    
def ggl(query, num_results=20):
    query  = query.replace(' ','+')
    url = f'https://www.google.com/search?hl=en&q={query}&num={num_results}'
    resp = get_url(url)
    tree = html.fromstring(resp.text)
    results = []
    elements = tree.xpath("//div[@class='g']")
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
        results.append(res)
    return results
