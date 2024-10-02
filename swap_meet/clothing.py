from .item import Item
class Clothing(Item):
    def __init__(self, id, fabric= "Unknown"):
        super().__init__(id, condition=0)
        self.fabric = fabric
        self.id = id


    def get_category():
        return "Clothing"
    
    def __str__(self):
        return (f"An object of type Clothing with id {self.id}.It is made from {self.fabric} fabric.")
    
