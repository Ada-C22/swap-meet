import uuid

class Decor:
    def __init__(self, id=None, width=0, length=0):
        self.id = uuid.uuid4().int if id is None else id
        self.width = width
        self.length = length
        self.condition = 0
    
    def get_category(self):
        return "Decor"
    
    def __str__(self): 
        return "An object of type Decor with id {}. It takes up a {} by {} sized space.".format(self.id, self.width, self.length)