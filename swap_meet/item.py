import uuid

class Item:
    
    def __init__(self, id):

        if not id:
            self.id = uuid.uuid4().int
        
        else:
            self.id = id
    
    # try dunder name class method
    def get_category(self):
        return "Item"