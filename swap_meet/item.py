import uuid

class Item:
    
    # wave 2
    def __init__(self, id=None, category="Item", condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.category = category # default
        self.condition = condition
    
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}."
    
    def get_category(self):
        return self.category
    
    # wave 3
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}."

    # wave 5 (DRY)
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
        else:
            return "No condition"
