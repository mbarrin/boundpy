import json
import requests

class Boundaryalias(requests.Session):
    """
    """
    def __init__(self, org_id, api_key):
        self.org_id = org_id
        self.api_key = api_key
        self.url = "https://api.boundary.com/%(org)s/" % {"org": self.org_id}
        super(Boundaryalias, self).__init__()
        self.headers = {"User-Agent": "mbarrin test",
                        "Content-Type": "application/json"}

    def get_ip_aliases(self):
        """
        """
        new_url = self.url + "aliases/ips"
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_ip_alias(self, ip):
        """
        """
        new_url = self.url + "aliases/ips/" + ip
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response.text
        else:
            return False

    def set_ip_alias(self):
        """
        """

    # Deletes existing
    def set_all_ip_aliases(self, payload):
        """
        """
        new_url = self.url + "aliases/ips/"
        req = requests.Request('PUT', new_url, auth=(self.api_key, ""), headers=self.headers, data=json.dumps(payload))
        r = req.prepare()
        response = self.send(r)
        return response

    # 6  = TCP
    # 17 = UDP
    def get_port_aliases(self):
        """
        """
        new_url = self.url + "aliases/ports"
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_port_alias(self, port):
        """
        """
        new_url = self.url + "aliases/ports/" + port
        req = requests.Request('GET', new_url, auth=(self.api_key, ""), headers=self.headers)
        r = req.prepare()
        response = self.send(r)
        if response.status_code == 200:
            return response.text
        else:
            return False

    # Deletes existing
    def set_all_port_aliases(self, payload):
        """
        """
        new_url = self.url + "aliases/ports/"
        req = requests.Request('PUT', new_url, auth=(self.api_key, ""), headers=self.headers, data=json.dumps(payload))
        r = req.prepare()
        response = self.send(r)
        return response

    def set_port_alias(self, port, alias):
        """
        """

