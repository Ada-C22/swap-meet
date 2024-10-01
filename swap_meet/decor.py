import uuid

class Decor:
    def __init__(self, id=None, width=0, length=0, condition=0):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
            
        self.width = width
        self.length = length
        self.condition=condition
        
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}.\
            This is a {self.type} device."