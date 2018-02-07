import aiohttp
import asyncio
from wikipydia import logs
from wikipydia import classes
import urllib

class Client:
    'Base client class for Wikipydia applications.'
    def __init__(self, token=None, username=None, password=None):
        if username and password:
            logs.warn('Username + password combinations are deprecated. Consider switching to OAuth2.')
        self.base_url = 'https://en.wikipedia.org/w/api.php' # enwiki default api
        self.page_burl = 'https://en.wikipedia.org/wiki/' # enwiki default page url
        self.rest_burl = 'https://en.wikipedia.org/api/rest_v1/' # enwiki default REST url
        self.cs = aiohttp.ClientSession()

    async def search_title(self, query:list):
        'Search for page titles.'
        if type(query) == str:
            query = query.split(',')
        query = [urllib.parse.quote_plus(i) for i in query]
        params = f'?action=query&titles={"|".join(query)}&format=json'
        final = self.base_url + params
        async with self.cs.get(final) as r:
            res = await r.json(content_type=None)
        pages = []
        for e, i in res['query']['pages'].items():
            if e == '-1':
                pages.append(classes.NotFoundPage(i['title']))
                continue
            pages.append(classes.Page(i['title'], i['pageid'], i['ns'], self.page_burl))
        pages = pages[0] if len(pages) == 1 else pages
        return pages

    def base(self, url, rest, page=None):
        'Changes the base URL for searches and API requests.'
        self.base_url = url
        self.rest_burl = rest
        if page: self.page_burl = page

    def close(self):
        self.cs.close()
