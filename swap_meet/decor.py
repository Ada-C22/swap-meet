from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, category="Decor")
        self.category = "Decor"
        self.condition = condition
        self.width = width
        self.length = length
    
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
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