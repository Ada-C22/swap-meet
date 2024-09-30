import uuid 
class Item:
    def __init__(self, id=None): 
        #each item should have a unique id using uuid
        self.id = uuid.uuid4().int
    
        self.category = str
    def get_category(self):
        # return #string of class
        self.category = "Clothing"
        self.category = "Decor"
        self.category = "Electronics"
