import wikipydia
# test script for wikipydia apps

import asyncio

async def test():
    c = wikipydia.client.Client()
    pages = await c.search_title(['Main Pa', 'MediaWiki'])
    print(pages)
    c.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
