from .item import Item
class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0, age=0):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} It is made from {self.fabric} fabric."
    
    