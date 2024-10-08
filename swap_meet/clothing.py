from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0, fabric="Unknown", id=None, age=0):
        super().__init__(id, condition, age)
        self.fabric = fabric
    
    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
