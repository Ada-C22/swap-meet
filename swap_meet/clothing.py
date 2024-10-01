from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id=id)
        self.fabric = fabric

    #Has a function `get_category` that returns `"Decor"
    #inheritance from Item class

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
        