import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"
        #can refactor to return the name of the class if time allows 
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 5:
            return "Brand new"
        elif self.condition == 4:
            return "Somewhat brand new"
        elif self.condition == 3:
            return "Used but not bad"
        elif self.condition == 2:
            return "Used"
        elif self.condition == 1:
            return "Really used"
        elif self.condition == 0:
            return "Ewwww"
        

        