from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric = "Unknown"):
        super().__init__(id, condition) # parent class Item id
        self.fabric = fabric
    
    # inherits Item method get_category

    # overrides Item method str
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."
    
# x = Clothing(123, 2)
# print(str(x))
    
