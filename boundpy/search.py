__author__ = 'matthew'

import requests

class search:
    def __init__(self):
        pass

    def annotation(self, payload):
        req = requests.Request('GET', self.url, auth=(self.api_key, ""),  params=payload, headers=self.headers)
        r = req.prepare()