from uuid import uuid4

class Item:
    def __init__(self, id=None,condition=0,age=0):
        self.id = uuid4().int if id is None else id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        condition = self.condition
        match condition:
            case condition if 0.0 <= condition < 2.0:
                return 'This is poor condition'
            case condition if 2.0 <= condition < 4.0:
                return 'It is gently used.'
            case condition if 4.0 < condition:
                return 'Fantastic condition'
            case _:
                return "Hmm...something's not right."