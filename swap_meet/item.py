from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return type(self).__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition > 5 or self.condition < 0:
            return "I don't know what to do with this."
        elif self.condition < 1:
            return "It's real bad."
        elif self.condition < 2:
            return "It's not great."
        elif self.condition < 3:
            return "It's okay."
        elif self.condition < 4:
            return "It's fine."
        elif self.condition < 5:
            return "It's great!"
        elif self.condition == 5:
            return "Mint condition!"