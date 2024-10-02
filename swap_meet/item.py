import uuid 

class Item:
    def __init__(self, id=None, condition=0): 
    # If id is passed, use it. Otherwise, generate a unique id using uuid
        self.id = id if id is not None else uuid.uuid4().int

    def get_category(self):
        # return string of class
        return "Item"

    def __str__(self):
        # id_str = str(self.id)
        return (f"An object of type Item with id {self.id}.") 
    
    def condition_description(self):
        if self.condition_description == 0:
            return "bad"
        elif self.condition_description == 1:
            return "so-so"
        elif self.condition_description == 2:
            return "as-is"
        elif self.condition_description == 3:
            return "ok"
        elif self.condition_description == 4:
            return "good"
        elif self.condition_description == 5:
            return "excellent"
        