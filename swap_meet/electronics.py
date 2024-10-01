import uuid

class Electronics:

    def __init__(self, id=None, type="Unknown", condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
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
    
