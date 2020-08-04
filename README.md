# SeReSoup
Combining requests and BeautifulSoup, Selenium

```batch
>>> from SeReSoup import *
>>> url = 'http://httpbin.org/get'
>>> res = ReSoup().soup(url)
>>> type(res)
requests.models.Response
>>>
>>> soup = ReSoup().soup(url , soup=True)
>>> type(soup)
bs4.BeautifulSoup

```

```batch
>>> from SeReSoup import *
>>> url = 'http://httpbin.org/get'
>>> soup = SeSoup().soup(url, mydriver=None , soup=True)
>>> type(soup)
bs4.BeautifulSoup

```
