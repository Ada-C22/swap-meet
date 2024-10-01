import uuid

class Decor:
    def __init__(self, id, type):
        self.id = int(uuid.uuid4())
        self.type = type
        
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}.\
            This is a {self.type} device."