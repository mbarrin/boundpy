__author__ = 'matthew'
class annotation(object):

    def __init__(self, annotation_id, annotation_type, annotation_subtype, creation_time, start_time, end_time, link, tags, loc=None):
        self.annotation_id = annotation_id
        self.annotation_type = annotation_type
        self.annotation_subtype= annotation_subtype
        self.creation_time = creation_time
        self.start_time = start_time
        self.end_time = end_time
        self.links = link
        self.tags = tags
        self.loc = loc
