import uuid
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} This is a {self.type} device."
