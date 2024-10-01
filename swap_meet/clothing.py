import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknown"):
        self.id = uuid.uuid4().int if id is None else id
        self.fabric = fabric
        self.condition = 0
    
    def get_category(self):
        return "Clothing"

    def __str__(self): 
        return "An object of type Clothing with id {}. It is made from {} fabric.".format(self.id, self.fabric)