import asyncio
import wikipydia

async def _test():
    c = wikipydia.Client()
    pages = await c.search_title('MediaWiki')
    c.close()
    print([p.title for p in pages if type(p) != wikipydia.NotFoundPage])

loop = asyncio.get_event_loop()
loop.run_until_complete(_test())
loop.close()
