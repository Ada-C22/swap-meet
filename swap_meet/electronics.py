import uuid
from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type
    
    def __str__(self):
        item_string = super().__str__()
        return f"{item_string} This is a {self.type} device."
