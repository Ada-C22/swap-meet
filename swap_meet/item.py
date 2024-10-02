import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def condition_description(self):
        descriptions = {
            0: "Ew no",
            1: "Look at other things to save time",
            2: "Very much used, but it's cheap",
            3: "Condition is acceptable for the worth",
            4: "Close to almost unused",
            5: "Almost unused"
        }
        return descriptions.get(self.condition, "Unknowned condition.")
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
