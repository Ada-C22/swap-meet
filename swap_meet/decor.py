import uuid
from swap_meet.item import Item

class Decor(Item):
    '''
    Refactored get_category method by inheriting from parent class Item
    # def get_category(self):
    #     return "Decor"
    '''

    def __init__(self, id=None, width=0, length=0, condition=0, age=None):
        super().__init__(id, condition, age)
        self.width = width
        self.length = length
    

    def __str__(self): 
        return "An object of type {} with id {}. It takes up a {} by {} sized space.".format(self.get_category(), self.id, self.width, self.length)