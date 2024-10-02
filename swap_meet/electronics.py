from .item import Item
class Electronics(Item):
    def __init__(self, id, type= "Unknown"):
        super().__init__(id, condition=0)
        self.type = type
        
    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
