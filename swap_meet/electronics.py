from .item import Item 

class Electronics(Item):

    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type
        
    def get_category(self):
        return "Electronics" 
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."
