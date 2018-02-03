import aiohttp
import asyncio
from wikipydia import logs
import urllib

class Client:
    'Base client class for Wikipydia applications.'
    def __init__(self, token=None, username=None, password=None):
        if username and password:
            logs.warn('Username + password combinations are deprecated. Consider switching to OAuth2.')
        self.base_url = 'https://en.wikipedia.org/w/api.php' # enwiki default api
        self.cs = aiohttp.ClientSession()

    async def search(self, query:list):
        if type(query) == str:
            query = query.split(',')
        query = [urllib.parse.quote_plus(i) for i in query]
        params = f'?action=query&titles={"|".join(query)}&format=json'
        final = self.base_url + params
        async with self.cs.get(final) as r:
            return await r.json(content_type=None)

    def close(self):
        self.cs.close()
