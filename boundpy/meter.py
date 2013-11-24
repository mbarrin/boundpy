__author__ = 'matthew'
class meter(object):

    def __init__(self, meter_id, name, obs_domain_id, cert_serial_number, org_id, created_at, updated_at, links, tags):
        self.meter_id = meter_id
        self.name = name
        self.obs_domain_id = obs_domain_id
        self.cert_serial_number= cert_serial_number
        self.org_id= org_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.links = links
        self.tags = tags


