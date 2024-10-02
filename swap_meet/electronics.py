from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id)
        self.category = "Electronics"
        self.type = type
        self.condition = condition

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
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
