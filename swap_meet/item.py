import uuid

class Item:
    def __init__(self,id=None):
        if id == None:
            id = uuid.uuid4().int
        self.id = id
    
    def get_category(self):
        return self.__class__.__name__
