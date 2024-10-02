import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    conditions = {0: "New", 1: "Mint", 2: "Good", 3: "Fair", 4: "Heavily used", 5: "Damaged"}

    def condition_description(self):
        return Item.conditions.get(self.condition, "Unknown")
