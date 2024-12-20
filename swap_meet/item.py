import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id == None else id
        self.condition = condition
    
    def __str__(self):
        return f"An object of type Item with id {self.id}"
    
    def get_category(self):
        return "Item"
    
    def condition_description(self):
        if self.condition == 5:
            return "Excellent"
        elif self.condition == 4:
            return "Very Good"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 2:
            return "Okay"
        elif self.condition == 1:
            return "Bad"



        