import uuid


class Clothing:
    
    def __init__(self, id=None, fabric="Unknown", condition=0 ): 
        self.id = uuid.uuid4().int if id is None else id
        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
    def condition_description(self):
        if self.condition == 5:
            return "Brand new"
        elif self.condition == 4:
            return "Somewhat brand new"
        elif self.condition == 3:
            return "Used but not bad"
        elif self.condition == 2:
            return "Used"
        elif self.condition == 1:
            return "Really used"
        elif self.condition == 0:
            return "Ewwww"
