import uuid 

class Item:
    def __init__(self, id=None, condition=None, age=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition if condition is not None else 0

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "You should seriously consider not taking this one."
        if self.condition > 0 and self.condition < 1:
            return "It's barely holding together."
        if self.condition >= 1 and self.condition < 2:
            return "This item has seen better days."
        if self.condition >= 2 and self.condition < 3:
            return "It is a bit worn, but still has life left."
        if self.condition >= 3 and self.condition < 4:
            return "In good condition."
        if self.condition >= 4 and self.condition < 5:
            return "Almost like new!"
        return "Mint condition."
