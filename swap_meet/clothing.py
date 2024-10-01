class Clothing:
    def __init__(self, id, fabric):
        self. id = id
        self.fabric = fabric
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. \
            It is made from {self.fabric} fabric."