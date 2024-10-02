import uuid

class Item:
    
    # wave 2
    def __init__(self, id=None, category="Item", condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.category = category # default
        self.condition = condition
    
    def get_category(self):
        return self.category
    

    #     # wave 2
    # def __init__(self, id=None):
    #     self.id = id if id is not None else uuid.uuid4().int

    # def get_category(self):
    #     return "Item"
    
    # wave 3
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}."

    # wave 5
    def condition_description(self):
        return "No condition"