import uuid
from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type
    
    def get_category(self):
        return "Electronics"
    
    def __str__(self): 
        return "An object of type {} with id {}. This is a {} device.".format(self.get_category(), self.id, self.type)
