
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=None, age=None):
        super().__init__(id,condition,age)
        self.type = type
    
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. "\
        f"This is a {self.type} device."