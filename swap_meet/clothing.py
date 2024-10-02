from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, id=None, fabric="Unknown"):
        
        super().__init__(id)
        self.fabric = fabric
        # self.fabric = fabric if not fabric is "Unknown" else fabric

    def get_category(self):
        return "Clothing" 

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."


