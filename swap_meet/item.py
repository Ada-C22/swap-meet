import uuid
# import random

class Item:
    
    def __init__(self, id=None):
        
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def get_category(self):
        return "Item"
    
    
