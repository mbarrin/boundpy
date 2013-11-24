import json
import requests

class Boundaryalert(requests.Session):
    """
    """
    def __init__(self, org_id, api_key):
        self.org_id = org_id
        self.api_key = api_key
        self.url = "https://api.boundary.com/%(org)s/" % {"org": self.org_id}
        super(Boundaryalert, self).__init__()
        self.headers = {"User-Agent": "mbarrin test",
                        "Content-Type": "application/json"}

    def create_alert(self, payload):
        new_url = self.url + "alerts"
        req = requests.Request('POST', new_url, auth=(self.api_key, ""),  data=json.dumps(payload), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 201:
            return True
        else:
            return False

    def get_all_alerts(self):
        new_url = self.url + "alerts"
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_alert(self, alert_id):
        new_url = self.url + "alerts/" + alert_id
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_alert_state(self, alert_id):
        new_url = self.url + "alerts/" + alert_id + "/state"
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def update_alert(self, alert_id, payload):
        new_url = self.url + "alerts/" + alert_id
        req = requests.Request('POST', new_url, auth=(self.api_key, ""),  data=json.dumps(payload), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 204:
            return True
        else:
            return False

    def delete_alert(self, alert_id):
        new_url = self.url + "alerts/" + alert_id
        req = requests.Request('DELETE', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 204:
            return True
        else:
            return False
