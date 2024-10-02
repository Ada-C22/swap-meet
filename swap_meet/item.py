import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = float(condition)

    def get_category(self):
        return type(self).__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 5:
            return "Brand New"
        elif self.condition == 4:
            return "Like New"
        elif self.condition == 3:
            return "Lightly Used"
        elif self.condition == 2:
            return "Moderately Used"
        elif self.condition == 1:
            return "Heavily Used"
        
        
    
