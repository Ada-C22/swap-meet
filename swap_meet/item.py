import uuid 

class Item:
    def __init__(self, id=None, condition=None, age= None):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition if condition is not None else 0
        self.age = age if age else None

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):

        if self.condition > 0 and self.condition < 1:
            return "It's barely holding together."
        elif self.condition >= 1 and self.condition < 2:
            return "This item has seen better days."
        elif self.condition >= 2 and self.condition < 3:
            return "It is a bit worn, but still has life left."
        elif self.condition >= 3 and self.condition < 4:
            return "In good condition."
        elif self.condition >= 4 and self.condition < 5:
            return "Almost like new!"
        return "Mint condition."


