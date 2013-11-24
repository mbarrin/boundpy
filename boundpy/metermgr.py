__author__ = 'matthew'

import requests
import json
import meter

class metermgr:

    def __init__(self, url, org_id, api_key, headers):
        self.url = url + "meters/"
        self.org_id = org_id
        self.api_key = api_key
        self.headers = headers
        self.session = requests.Session()

    #works
    def read_all(self):
        """
        Returns a list of meter objects
        """
        all_meters = []
        r = self.session.get(self.url, auth=(self.api_key, ""), headers=self.headers)
        for meter in r.json():
            all_meters.append(self.data2meter(meter))
        return all_meters

    #works
    def read(self, meter_id):
        """
        Returns a meter object from the passed id
        """
        url = self.url + meter_id
        r = self.session.get(url, auth=(self.api_key, ""), headers=self.headers)
        return self.data2meter(r.json())

    #works
    def search(self,name):
        """
        Search for a meter based on name. Tags will be added. Returns a list of meters
        """
        results = []
        payload = {"name" : name}
        r = self.session.get(self.url, auth=(self.api_key, ""), params=payload, headers=self.headers)
        for meter in r.json():
            results.append(self.data2meter(meter))
        return results

    def create(self):
        """
        Creates a meter with the passed details
        """
        payload = {"name": "mbarrintest"}
        r = self.session.put(self.url, auth=(self.api_key, ""),  data=json.dumps(payload), headers=self.headers)
        return r

    def add_tag(self, meter_id, tag):
        """
        Adds the given tag to the given meter
        """
        tag_suffix = meter_id + "/tags/" + tag
        r =  self.session.put(self.url + tag_suffix, auth=(self.api_key, ""), headers=self.headers)
        if r.status_code == 204:
            return True
        else:
            return False

    def check_tag(self, meter_id, tag):
        """
        Checks if the given tag exists on the given meter
        """
        tag_suffix = meter_id + "/tags/" + tag
        r =  self.session.get(self.url + tag_suffix, auth=(self.api_key, ""), headers=self.headers)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            return False

    def delete_tag(self, meter_id, tag):
        """
        Deletes the given tag from the given meter
        """
        tag_suffix = meter_id + "/tags/" + tag
        r =  self.session.delete(self.url + tag_suffix, auth=(self.api_key, ""), headers=self.headers)
        if r.status_code == 204:
            return True
        else:
            return False

    def delete(self, meter_id):
        """
        Deletes the given meter
        """
        #204 succeed
        #404 failure
        r = self.session.delete(self.url, auth=(self.api_key, ""), headers=self.headers)
        if r.status_code == 204:
            return True
        elif r.status_code == 404:
            return False

    def pub_cert(self):
        return True

    def private_key(self):
        return True

    def data2meter(self, response):
        return meter.meter(response["id"], response["name"], response["obs_domain_id"], response["cert_serial_number"], response["org_id"], response["created_at"], response["updated_at"], response["links"], response["tags"])

    def meter2data(self, x):
        return { "id": x.id,
                "name": x.name,
                "obs_domain_id": x.obs_domain_id,
                "cert_serial_number": x.cert_serial_number,
                "org_id": x.org_id,
                "created_at": x.created_at,
                "updated_at": x.updated_at,
                "links": x.links,
                "tags": x.tags,
                }

