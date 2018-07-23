import asyncio
import mw4py

async def _test():
    c = mw4py.Client()
    pages = await c.search_title('MediaWiki')
    c.close()
    print([p.title for p in pages if type(p) != mw4py.NotFoundPage])

loop = asyncio.get_event_loop()
loop.run_until_complete(_test())
loop.close()
