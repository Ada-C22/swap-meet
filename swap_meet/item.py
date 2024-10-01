import uuid

class Item:
    def __init__(self,id=None):
        if id == None:
            id = uuid.uuid4().int
        self.id = id
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {str(self.id)}."
        
