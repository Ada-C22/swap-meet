import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknow",condition=0):
        if id is None:
            self. id = int(uuid.uuid4())
        else:
            self.id = id
            
        self.fabric = fabric
        self.condition = condition
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. \
            It is made from {self.fabric} fabric."