import uuid

class Item:
    def __init__(self, id=None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__
    
    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id
        return False  
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
i = Item()
x = i.get_category()
print(type(x))