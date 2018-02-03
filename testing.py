import wikipydia
# test script for wikipydia apps

import asyncio

async def test():
    c = wikipydia.client.Client()
    print(await c.search(['Main Page', 'MediaWiki'])) # yay multi page titles
    c.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
