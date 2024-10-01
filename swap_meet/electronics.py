import uuid

class Electronics:
    def __init__(self, id=None, type="Unknown"):
        self.id = uuid.uuid4().int if id is None else id
        self.type = type
        self.condition = 0
    
    def get_category(self):
        return "Electronics"
    
    def __str__(self): 
        return "An object of type Electronics with id {}. This is a {} device.".format(self.id, self.type)
