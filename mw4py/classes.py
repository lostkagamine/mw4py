
# mw4py classes
# don't touch these or you'll break the module

import asyncio

class Page:
    def __init__(self, title, id, ns, baseurl):
        self.baseurl = baseurl
        self.url = baseurl + title.replace(' ', '_')
        self.id = id
        self.ns = ns
        self.title = title

class NotFoundPage:
    def __init__(self, title):
        self.title = title
