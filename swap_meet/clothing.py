from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0,fabric="Unknown"):
        super().__init__(id, category="Clothing")
        self.condition = condition
        self.fabric = fabric
    
    
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}. It is made from {self.fabric} fabric."
    
    def condition_description(self):
        if self.condition == 0:
            return "Brand new"
        elif self.condition ==1:
            return "Gently used"
        elif self.condition == 2:
            return "Used"
        elif self.condition == 3:
            return "Well used"
        elif self.condition == 4:
            return "Heavily used"
        elif self.condition == 5:
            return "Heavily worn"
        
        return "Unknown condition"