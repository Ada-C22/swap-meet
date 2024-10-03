import uuid
from swap_meet.item import Item

class Electronics(Item):
    '''
    Refactored get_category method by inheriting from parent class Item
    # def get_category(self):
    #     return "Electronics"
    '''

    def __init__(self, id=None, type="Unknown", condition=0, age=None):
        super().__init__(id, condition, age)
        self.type = type


    def __str__(self): 
        return "An object of type {} with id {}. This is a {} device.".format(self.get_category(), self.id, self.type)
