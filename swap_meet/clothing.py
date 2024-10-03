import uuid
from swap_meet.item import Item

class Clothing(Item):
    '''
    Refactored get_category method by inheriting from parent class Item
    # def get_category(self):
    #     return "Clothing"
    '''

    def __init__(self, id=None, fabric="Unknown", condition=0, age=None):
        super().__init__(id, condition, age)
        self.fabric = fabric


    def __str__(self): 
        return "An object of type {} with id {}. It is made from {} fabric.".format(self.get_category(), self.id, self.fabric)

