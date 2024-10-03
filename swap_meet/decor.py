from .item import Item

class Decor(Item):
    def __init__(self,id=None, condition=0,width=0, length=0, age=None):
        super().__init__(id, condition, age)
        self.width = width
        self.length = length
    
    def __str__(self):
        return  f"An object of type Decor with id {self.id}. "\
                f"It takes up a {self.width} by {self.length} sized space. "\
                f"It was produced on {self.age.strftime("%x")}."