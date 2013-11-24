import json
import requests

__author__ = 'matthew'


class Boundarysession(requests.Session):
    """
    """
    def __init__(self, org_id, api_key):
        self.org_id = org_id
        self.api_key = api_key
        self.url = "https://api.boundary.com/%(org)s/" % {"org": self.org_id}
        super(Boundarysession, self).__init__()
        self.headers = {"User-Agent": "mbarrin test",
                        "Content-Type": "application/json"}

    def search(self, types=None, query="[*:*]", start=0, rows=100,
                bodies=True, buckets=None, bucket_sort=None, debug=True):

        """
        Returns a dict
        :param debug:
        :param types:
        :param query:
        :param start:
        :param rows:
        :param bodies:
        :param buckets:
        :param bucket_sort:
        """
        if not types:
            types = ["annotation", "meter"]

        search_query = {
            "types": types,
            "query": query,
            "start": start,
            "rows": rows,
            "bodies": bodies,
            "buckets": buckets,
            "bucketsort": bucket_sort,
            "debug": debug
        }
        new_url = self.url + "search"
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), \
                params=search_query, headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response
        else:
            return None

    def create_stored_search(self, types="meter", query="[*:*]", start=0, rows=100, bodies=True, buckets=None, bucket_sort=None,
               debug=True):
        """

        Can use annotation but will break things. Boundary said they plan to do something to change it`


        :param types:
        :param query:
        :param start:
        :param rows:
        :param bodies:
        :param buckets:
        :param bucket_sort:
        :param debug:
        """
        search_query = {
            "types": types,
            "query": query,
            "start": start,
            "rows": rows,
            "bodies": bodies,
            "buckets": buckets,
            "bucketsort": bucket_sort,
            "debug": debug
        }
        new_url = self.url + "searches"
        req = requests.Request('POST', new_url, auth=(self.api_key, ""), data=json.dumps(search_query), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 201:
            return response.headers['location']
        else:
            return False

    def delete_stored_search(self, search_id=None):
        new_url = self.url + "searches/" + search_id
        req = requests.Request('DELETE', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 204:
            return True
        else:
            return None

    def get_stored_search(self, search_id=None):
        new_url = self.url + "searches/" + search_id + "/results"
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response
        else:
            return None

    def get_stored_searches(self):
        new_url = self.url + "searches"
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response
        else:
            return None

    def data2annotation(self, response):
        return annotation.annotation(response["id"], response["type"], response["subtype"], response["creation_time"], response["start_time"], response["end_time"], response["links"], response["tags"], response["loc"])

    def annotation2data(self, annotation):

        return {"id": annotation.annotation_id,
                "type": annotation.annotation_type,
                "subtype": annotation.annotation_subtype,
                "creation_time": annotation.creation_time,
                "start_time": annotation.start_time,
                "end_time": annotation.end_time,
                "links": annotation.links,
                "tags": annotation.tags,
                "loc": annotation.loc
        }
