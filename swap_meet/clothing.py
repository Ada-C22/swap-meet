from .item import Item

class Clothing:
    def __init__(self,id=Item().id, fabric= "Unknown"):
        
        self.id = id
        self.fabric = fabric
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."  
    
    def get_category(self):
        return "Clothing"
        