import uuid
from swap_meet.vendor import Vendor

class Item:
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id
        self.name = "Item"

    def get_category(self):
        return self.name