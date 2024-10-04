from uuid import uuid4

class Item:
    def __init__(self, id=None,condition=0,age=0):
        self.id = uuid4().int if id is None else id
        self.condition = condition
        self.age = age

    def get_category(self):
        return type(self).__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition <= 2.0:
            return "This is poor condition."
        elif self.condition <= 4.0:
            return "It is gently used."
        elif self.condition > 4.0:
            return "Fantastic condition!"