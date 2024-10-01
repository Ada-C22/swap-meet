import uuid

class Decor:

    def __init__(self, id=None, width=0, length=0, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.width = width
        self.length = length
        self.condition = condition
    

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
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
    
    

    