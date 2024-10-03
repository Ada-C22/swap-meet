import uuid

class Item:
    def __init__(self, id=None,condition=0.0, age=0):
        self.id = uuid.uuid4().int if id is None else id
        self.name = "Item"
        self.condition = condition
        self.age = age

    def __str__(self):
        return f"An object of type {self.name} with id {self.id}."
    
    def get_category(self):
        return self.__class__.__name__
    
    def condition_description(self):
        if self.condition >=4 :
            return "like new"
        if 2 <= self.condition < 4:
            return "It's ok"
        return "Maybe you want to pick another one"