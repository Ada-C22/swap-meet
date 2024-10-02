import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric
    
    def get_category(self):
        return "Clothing"

    def __str__(self): 
        return "An object of type {} with id {}. It is made from {} fabric.".format(self.get_category(), self.id, self.fabric)

