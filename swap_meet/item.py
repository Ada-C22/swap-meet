import uuid

class Item:
    def __init__(self, id=None):
        id = int(uuid.uuid4()) if not id else id
        self.id = id

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
import uuid

class Item:
    def __init__(self, id=int(uuid.uuid4())):
        self.id = id

    def get_category(self):
        return "Item"