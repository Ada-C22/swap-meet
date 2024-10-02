from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition) # parent class Item id
        self.type = type
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."