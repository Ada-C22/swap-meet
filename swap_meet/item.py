import uuid 

class Item:
    def __init__(self, id=None, condition=None):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition if condition is not None else 0
    def get_category(self):
        return type(self).__name__
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    def condition_description(self):
        if self.condition == 0:
            return "You should seriously consider not taking this one"
        elif self.condition < 1:
            return "It's barely holding together."
        elif self.condition < 2:
            return "This item has seen better days."
        elif self.condition < 3:
            return "It is a bit worn, but still has life left."
        elif self.condition < 4:
            return "In good condition"
        elif self.condition < 5:
            return "Almost like new!"
        else:
            return "Mint condition"