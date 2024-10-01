import uuid

class Item:
    def __init__(self, id = None):
        self.id = uuid.uuid4().int if id is None else id
        self.name = "Item"

    def get_category(self):
        return self.name

    # def get_by_id(self, id):
    #     inventory = Vendor.inventory

    #     if id not in inventory:
    #         return None
    #     return Vendor.id