import uuid

class Item:
    def __init__(self, id=int(uuid.uuid4())):
        self.id = id

    def get_category(self):
        return "Item"