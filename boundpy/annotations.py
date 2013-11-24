__author__ = 'matthew'
import json
import requests
import annotation

class annotations():

    def __init__(self, url, org_id, api_key, headers):
        self.url = url + "annotations"
        self.org_id = org_id
        self.api_key = api_key
        self.headers = headers
        self.session = requests.Session()

    #Works

