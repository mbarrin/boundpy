import json
import requests

__author__ == 'matthew'

class Boundaryannotation(requests.Session):
    """
    """
    def __init__(self, org_id, api_key):
        self.org_id = org_id
        self.api_key = api_key
        self.url = "https://api.boundary.com/%(org)s/" % {"org": self.org_id}
        super(Boundaryannotation, self).__init__()
        self.headers = {"User-Agent": "mbarrin test",
                        "Content-Type": "application/json"}

    def create_annotation(self, payload):
        """
        Returns a True if the create succeeds
        :param payload:
        """
        #TODO have it return the link instead of True/False
        new_url = self.url + "annotations"
        req = requests.Request('POST', new_url, auth=(self.api_key, ""),  data=json.dumps(payload), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 201:
            return True
        else:
            return False

    def view_annotation(self, annotation_id):
        """
        Returns an annotation object referenced by the passed id
        """
        new_url = self.url + "annotations/" + annotation_id
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        print response.status_code
        return response

    def delete_annotation(self, annotation_id):
        """
        Deletes the given annotation
        """
        new_url = self.url + "annotations/" + annotation_id
        req = requests.Request('DELETE', new_url, auth=(self.api_key, ""), headers=self.headers)
        r =  req.prepare()
        response = self.send(r)
        print response.status_code
        return response

    def edit_annotation(self, annotation_id, payload):
        """
        Edits the given annotation
        """
        new_url = self.url + "annotations/" + annotation_id
        req = requests.Request('PUT', new_url, auth=(self.api_key, ""),  data=json.dumps(payload), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 201:
            return True
        else:
            print response.status_code
            return False

    def add_link_to_annotation(self, annotation_id, payload):
        new_url = self.url + "annotations/" + annotation_id + "/links"
        req = requests.Request('POST', new_url, auth=(self.api_key, ""), data=json.dumps(payload), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 201:
            return True
        else:
            return False

    def add_tag_to_annotation(self, annotation_id, tag):
        new_url = self.url + "annotations/" + annotation_id + "/" +  tag
        req = requests.Request('PUT', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        return response
