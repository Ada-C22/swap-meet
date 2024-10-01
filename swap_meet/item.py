import uuid

class Item:
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id
        self.name = "Item"

    def __str__(self):
        return f"An object of type {self.name} with id {self.id}."
    
    def get_category(self):
        return self.name