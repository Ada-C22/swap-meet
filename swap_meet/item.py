import uuid 

class Item:
    def __init__(self, id=None, category="Item"): 
    # If id is passed, use it. Otherwise, generate a unique id using uuid
        self.id = id if id is not None else uuid.uuid4().int
        self.category = category

    def get_category(self):
        # return string of class
        return self.category

    def __str__(self):
        id_str = str(self.id)
        return (f"An object of type Item with id {id_str}.")