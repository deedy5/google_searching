![Python >= 3.6](https://img.shields.io/badge/python->=3.6-red.svg) [![](https://badgen.net/github/release/deedy5/google_searching)](https://github.com/deedy5/google_searching/releases) [![](https://badge.fury.io/py/google-searching.svg)](https://pypi.org/project/google_searching) 
## Google_searching

Google.com search results.

### Install
```python
pip install -U google_searching
```

### Usage
*WARNING!: the site gives an captcha when making frequent repeated requests.* <br/> Call ggl() function again after at least **5 seconds.**
```python
from google_searching import ggl

ggl(keywords, lang='en', max_results=20):
    ''' Google search
    keywords: keywords for query,
    lang: language of search results,
    max_results: not limited, in practice about 500.
    '''
```
### Returns
```python
[
{'title': title of result,
  'href': href of result,
  'body': body of result},
...
]
```

### Example
```python3
from google_searching import ggl

r = ggl('usa', lang='en', max_results=100)
print(r)
```
